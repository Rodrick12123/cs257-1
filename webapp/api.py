'''
    api.py
    Rodrick and Thea, 09 November 2021

'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

def get_connection():
    ''' Returns a connection to the database described in the
        config module. May raise an exception as described in the
        documentation for psycopg2.connect. '''
    return psycopg2.connect(database=config.database,
                            user=config.user,
                            password=config.password)

@api.route('/Allcups/teams/') 
def get_all_teams():
    
    query = '''SELECT teams.team_abbreviation, teams.team_name 
                FROM teams ORDER BY teams.team_name;'''
    # mostG = flask.request.args.get('scores')
    # if mostG == 'top':
    #     query = '''SELECT teams.team_abbreviation, teams.team_name, players_teams_matches_worldcups.goal 
    #             FROM teams, players_teams_matches_worldcups
    #              ORDER BY players_teams_matches_worldcups.goal;'''
    # sort_argument = flask.request.args.get('sort')
    # if sort_argument == 'birth_year':
    #     query += 'birth_year'
    # else:
    #     query += 'surname, given_name'
    #query += 'team_name'

    team_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            team = {  'team_abbreviation':row[0],
                      'team_name':row[1]}
            team_list.append(team)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(team_list)

@api.route('/Allcups/')
def get_all_worldcups():
    
    query = '''SELECT worldcups.year, worldcups.location FROM worldcups ORDER BY worldcups.year;'''

    wc_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            wc = {  'wc_year':row[0],
                    'wc_location':row[1]}
            wc_list.append(wc)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(wc_list)


@api.route('/<years>/teams/') 
def get_teams(years):
    #must figure how this out 
    yrs = years.split(",")
    ymap = map(int, yrs)
    ylist = list(ymap)
    
    query = '''SELECT DISTINCT teams.team_abbreviation, teams.team_name, worldcups.year
               FROM worldcups, teams, players_teams_matches_worldcups
               WHERE players_teams_matches_worldcups.team_id = teams.id
                 AND players_teams_matches_worldcups.worldcup_id = worldcups.id
               ORDER BY worldcups.year'''
    team_list = []
    #yrs.sort()
    print(ylist)
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, )
        # cursor.execute(query, (years,))
        for row in cursor:
            if (row[2] in ylist):
                
                team = {'teamyear':row[2], 'team_abbreviation':row[0], 'team_name':row[1]}
                team_list.append(team)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(team_list)


@api.route('/<teams>/players/') 
def get_players():
    ''' Returns a list of all the authors in our database. See
        get_author_by_id below for description of the author
        resource representation.
        By default, the list is presented in alphabetical order
        by surname, then given_name. You may, however, use
        the GET parameter sort to request sorting by birth year.
            http://.../authors/?sort=birth_year
        Returns an empty list if there's any database failure.
    '''

    query = '''SELECT players.playerid, players.tmid, players.firstname, players.lastname, players.captain, players.starter, 
                teams.team_abbreviation, players.pnumber, players.position
               FROM players, teams 
               WHERE teams.teamid = players.tmid
               ORDER BY teams.team_abbreviation'''

    # sort_argument = flask.request.args.get('sort')
    # if sort_argument == 'birth_year':
    #     query += 'birth_year'
    # else:
    #     query += 'surname, given_name'
    query += 'lastname, surname'
    
    player_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query,)
        for row in cursor:
            if(row[5] in teams):
                player = {'plaerid':row[0],
                        'tmid':row[1],
                        'firstname':row[2],
                        'lastname':row[3],
                        'captain':row[4],
                        'starter':row[4],
                        'team_abbreviation':row[5],
                        'number':row[6],
                        'position':row[7]}
                player_list.append(player)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(player_list)

@api.route('/teams/gold/') 
def get_gold():
    
    query = '''SELECT teams.team_abbreviation, teams.team_name, worldcups.year, worldcups.firstplace
                FROM teams, worldcups 
                WHERE players_teams_matches_worldcups.team_id = teams.id
                 AND players_teams_matches_worldcups.worldcup_id = worldcups.id
                ORDER BY teams.team_name;'''
    team_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            if( worldcups.firstplace == teams.team_name):
                team = {'Abbreviation':row[0],
                        'Team Name':row[1],
                        'Worldcup':row[2]}
                team_list.append(team)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(team_list)

@api.route('/topscores') 
def get_gold():
    
    query = '''SELECT players.surname, players.given_name, players.coach
                FROM players, worldcups 
                WHERE players_teams_matches_worldcups.team_id = teams.id
                 AND players_teams_matches_worldcups.worldcup_id = worldcups.id
                ORDER BY teams.team_name;'''
    team_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            if( worldcups.firstplace == teams.team_name):
                team = {'Abbreviation':row[0],
                        'Team Name':row[1],
                        'Worldcup':row[2]}
                team_list.append(team)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(team_list)