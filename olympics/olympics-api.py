#Written by Thea Traw

import sys
import argparse
import flask
import json
import psycopg2
import config

app = flask.Flask(__name__)


#this class is to handle the interactions with the database
class Querier:

    def __init__(self):

        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password)
            self.cursor = connection.cursor()
        except Exception as e:
            print(e)
            exit()

    def handle_games_query(self):
        #returns a json list of all the olympic games (each as a dictionary) 

        all_games = []

        try:

            query = '''SELECT * FROM games ORDER BY games.year;'''

            self.cursor.execute(query)

            for row in self.cursor:
                current_games_dictionary = {'id':row[0], 'year':row[1], 'season':row[2], 'city':row[3]}
                all_games.append(current_games_dictionary)

            return json.dumps(all_games)

        except Exception as e:
            print(e)
            quit()


    def handle_nocs_query(self):
        #returns a json list of all the NOCs (each as a dictionary)

        all_nocs = []

        try:
            query = '''SELECT nocs.noc, nocs.region FROM nocs ORDER BY nocs.noc;'''

            self.cursor.execute(query)
            
            for row in self.cursor:
                current_noc_dictionary = {'abbreviation':row[0], 'name':row[1]}
                all_nocs.append(current_noc_dictionary)

            return json.dumps(all_nocs)

        except Exception as e:
            print(e)
            quit()  


    def handle_medalists_query(self, games_id):
        #returns a json list of all the medaling athletes (each as a dictionary) in a specified game (or, if a NOC is specified, returns only the medaling athletes that competed for that team)

        medalists = []
        search_string_noc = flask.request.args.get('noc')
        search_string_games_id = games_id

        try:
            if search_string_noc is not None:

                query = '''SELECT athletes.id, athletes.fullname, athletes.sex, events.sport, events.event, nocs_athletes_events_games.medal
FROM athletes, nocs, events, games, nocs_athletes_events_games
WHERE athletes.id = nocs_athletes_events_games.athlete_id
AND nocs.id = nocs_athletes_events_games.noc_id
AND events.id = nocs_athletes_events_games.event_id
AND games.id = nocs_athletes_events_games.games_id
AND nocs_athletes_events_games.medal != 'NA'
AND games.id = %s
AND LOWER(nocs.noc) = LOWER(%s);'''

                self.cursor.execute(query, (search_string_games_id, search_string_noc))

            else:

                query = '''SELECT athletes.id, athletes.fullname, athletes.sex, events.sport, events.event, nocs_athletes_events_games.medal
FROM athletes, nocs, events, games, nocs_athletes_events_games
WHERE athletes.id = nocs_athletes_events_games.athlete_id
AND nocs.id = nocs_athletes_events_games.noc_id
AND events.id = nocs_athletes_events_games.event_id
AND games.id = nocs_athletes_events_games.games_id
AND nocs_athletes_events_games.medal != 'NA'
AND games.id = %s;'''

                self.cursor.execute(query, (search_string_games_id,))

            for row in self.cursor:
                current_medalist_dictionary = {'athlete_id':row[0], 'athlete_name':row[1], 'athlete_sex':row[2], 'sport':row[3], 'event':row[4], 'medal':row[5]}
                medalists.append(current_medalist_dictionary)

            return json.dumps(medalists)

        except Exception as e:
            print(e)
            quit()


#create global variable of Querier() class to access in the @app.route-decorated functions
querier = Querier()

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/games')
def get_all_games():
    ''' Returns a list of all olympic games, sorted by year (oldest to most recent). '''

    return querier.handle_games_query()


@app.route('/nocs')
def get_all_nocs():
    '''Returns a list of all nocs, sorted alphabetically.'''

    return querier.handle_nocs_query()


@app.route('/medalists/games/<games_id>')
def get_all_medalists(games_id):
    ''' Returns the list of medalists in a given olympic games (specified by the unique games_id). An NOC can be given also, in which case only the medaling athletes of that team are returned. 
    '''

    return querier.handle_medalists_query(games_id)


def main():
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)

if __name__ == '__main__':
    main()
