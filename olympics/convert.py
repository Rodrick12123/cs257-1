#Written by Thea Traw

import csv

#USING noc_regions.csv

nocs = {}

noc_regions_data_file = open('noc_regions.csv')
noc_regions_reader = csv.reader(noc_regions_data_file)

nocs_data_file = open('nocs.csv', 'w')
nocs_writer = csv.writer(nocs_data_file)

heading_row = next(noc_regions_reader)
for row in noc_regions_reader:
    noc = row[0]
    region = row[1]
    if noc not in nocs:

        #deal with Singapore
        if noc == "SIN":
            noc = "SGP"

        noc_id = len(nocs) + 1
        nocs[noc] = [noc_id, region] 
        nocs_writer.writerow([noc_id, noc, region])

nocs_data_file.close()

#USING athletes_events.csv

athlete_events_data_file = open('athlete_events.csv')
athlete_events_reader = csv.reader(athlete_events_data_file)

#dictionaries
athletes = {}
events = {}
games = {}

#all file writers

athletes_file = open('athletes.csv', 'w')
athletes_writer = csv.writer(athletes_file)

events_file = open('events.csv', 'w')
events_writer = csv.writer(events_file)

games_file = open('games.csv', 'w')
games_writer = csv.writer(games_file)

nocs_athletes_events_games_file = open('nocs_athletes_events_games.csv', 'w')
nocs_athletes_events_games_writer = csv.writer(nocs_athletes_events_games_file)


#helper functions

def add_athlete_entry(row, writer):
    athlete_id = row[0]

    full_name = row[1]

    #will only consider very last word to be surname

    name_components = full_name.split(' ')

    surname = name_components[-1]
    surname_index = -1

    if surname == 'Jr.' or surname.find('(') != -1 or surname == 'III':
        surname = name_components[-2] + ' ' + surname
        surname_index = -2

    #given name is the rest
    given_name = ''
    for component in name_components[:surname_index]:
        given_name += component + ' '
    given_name = given_name[:len(given_name) - 1] #eliminates final space after given name

    #handle nickname
    nickname = 'NA'
    if given_name.find('"') != -1:
        given_name_components = given_name.split('"')
        given_name = given_name_components[0].strip(' ')
        nickname = given_name_components[1].strip('"')
    
    if athlete_id not in athletes:
        athletes[athlete_id] = [surname, given_name, nickname]
        writer.writerow([athlete_id, surname, given_name, nickname])

def add_event_entry(row, writer):
    event_name = row[13]
    sport = row[12]
    if event_name not in events:
        event_id = len(events) + 1
        events[event_name] = [event_id, sport]
        writer.writerow([event_id, event_name, sport])

def add_games_entry(row, writer):
    #each key will be the year of the given Olympic games                                  
    games_year = row[9]
    season = row[10]
    city = row[11]
    if games_year not in games:
        games_id = len(games) + 1
        games[games_year] = [games_id, season, city]
        writer.writerow([games_id, games_year, season, city])


def add_nocs_athletes_events_games_entry(row, writer):

    noc_name = row[7]
    athlete_id = row[0]
    event_name = row[13]
    medal = row[14]
    games_year = row[9]
    
    noc_id = nocs[noc_name][0]
    games_id = games[games_year][0]
    event_id = events[event_name][0]

    writer.writerow([noc_id, athlete_id, event_id, games_id, medal])


#go through all in lines in athlete_events.csv (except first line)
heading_row = next(athlete_events_reader) #skip first line (from Jeff's example code)
for row in athlete_events_reader:

    add_athlete_entry(row, athletes_writer)
    add_event_entry(row, events_writer)
    add_games_entry(row, games_writer)
    add_nocs_athletes_events_games_entry(row, nocs_athletes_events_games_writer)

athlete_events_data_file.close()
athletes_file.close()
events_file.close()
games_file.close()
nocs_athletes_events_games_file.close()
