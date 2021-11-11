''' 
File Converter
'''
import csv

#USING worldcups.csv

world_cups = {}

world_cups_data_file = open('worldcupsdata.csv')
world_cups_reader = csv.reader(world_cups_data_file)

world_cups_file = open('worldcups.csv', 'w')
world_cups_writer = csv.writer(world_cups_file)

heading_row = next(world_cups_reader)
for row in world_cups_reader:

    year = row[0]
    country = row[1]
    #teams on the podium
    first = row[2]
    second = row[3]
    third = row[4]
    fourth = row[5]
    attendance = row[9]

    #these should get deleted later, can use to confirm linking table works though, later
    #maybe don't add them yet? only if there's an issue they could help with?
    goals_scored = row[6]
    qualified_teams = row[7]
    matches_played = row[8]

    if year not in world_cups:
        wc_id = len(world_cups) + 1
        world_cups[year] = [wc_id, year, country, first, second, third, fourth, attendance, goals_scored] #maybe assign these values? like 'wc_id':wc_id? return to this 
        world_cups_writer.writerow([wc_id, year, country, first, second, third, fourth, attendance, goals_scored])

world_cups_file.close()
world_cups_data_file.close()

################################################


#USING worldcupmatches.csv                                                                                  

world_cup_matches_data_file = open('worldcupmatchesdata.csv')
world_cup_matches_reader = csv.reader(world_cup_matches_data_file)

#dictionaries                                                                                                
teams = {}
matches = {}

#all file writers                                                                                            
teams_file = open('teams.csv', 'w')
teams_writer = csv.writer(teams_file)

matches_file = open('matches.csv', 'w')
matches_writer = csv.writer(matches_file)


#give some specific attention to 

def add_match_entry(row, writer):

    match_id = row[17]

    if match_id == '':
        pass

    else:

        date_time = row[1]
        stage = row[2]
        home_team = row[5]
        home_team_score = int(row[6])
        away_team = row[8]
        away_team_score = int(row[7])
        win_conditions = row[9] #mostly empty, if not, regards extra time
        attendance = row[10]
        
    #first-half performance
        home_team_first_half_goals = int(row[11])
        away_team_first_half_goals = int(row[12])
        
    #second-half performance
        
    #checking for issue with weird data at the end....
        
        home_team_second_half_goals = home_team_score - home_team_first_half_goals
        away_team_second_half_goals = away_team_score - away_team_first_half_goals

        stadium = row[3]
        city = row[4]
        year = row[0]

        if match_id not in matches:
            matches[match_id] = [year, date_time, stage, stadium, city, home_team, home_team_score, away_team, away_team_score, win_conditions, attendance, home_team_first_half_goals, home_team_second_half_goals, away_team_first_half_goals, away_team_second_half_goals]
            
            writer.writerow([match_id, date_time, stage, stadium, city, home_team, home_team_score, away_team, away_team_score, win_conditions, attendance, home_team_first_half_goals, home_team_second_half_goals, away_team_first_half_goals, away_team_second_half_goals])

def add_teams_entry(row, writer): #this will add two team entries at once (so need to change title, else change how this works.....okay for now)
    home_team = row[5]
    home_team_abbreviation = row[18]
    away_team = row[8]
    away_team_abbreviation = row[19]

    if home_team_abbreviation not in teams:
        team_id = len(teams) + 1
        teams[home_team_abbreviation] = [team_id, home_team]
        writer.writerow([team_id, home_team_abbreviation, home_team])

    #exact same code, maybe a helper function because it's not particularly slick
    if away_team_abbreviation not in teams:
        team_id = len(teams) + 1
        teams[away_team_abbreviation] = [team_id, away_team]
        writer.writerow([team_id, away_team_abbreviation, away_team])

#go through all in lines in world_cup_matches.csv (except first line)
heading_row = next(world_cup_matches_reader) #skip first line (from Jeff's example code)
for row in world_cup_matches_reader:
    
    add_match_entry(row, matches_writer)
    add_teams_entry(row, teams_writer)

matches_file.close()
teams_file.close()
world_cup_matches_data_file.close()

##############################################################

#USING worldcupplayers.csv

world_cup_players_data_file = open('worldcupplayersdata.csv')
world_cup_players_reader = csv.reader(world_cup_players_data_file)

players_teams_matches_worldcups_file = open('players_teams_matches_worldcups.csv', 'w')
players_teams_matches_worldcups_writer = csv.writer(players_teams_matches_worldcups_file)

#dictionaries (not all of these are filled by this one file, reorganization would be nice--in progress)
players = {}

#all file writers

players_file = open('players.csv', 'w')
players_writer = csv.writer(players_file)

#helper functions

def process_name_into_parts(full_name):

    name_components = full_name.split(' ')

    surname = ''
    given_name = ''
    for component in name_components:

        #deal with the parentheses in coach names (idk why those are even there, maybe there's a mismatch somewhere?)
        if '(' in component and ')' in component: #only actually need one of these checks
            pass #just ignore, will get this information somewhere else

        elif component.isupper():
            surname = surname + ' ' + component
        else:
            given_name = given_name + ' ' + component


    #remove the extra spaces after the surname and given_name
    #surname = surname[:-1]
    #given_name = given_name[:-1]
    
    return [surname, given_name]

def add_player_entry(row, writer):

    full_name = row[6]

    processed_player_name = process_name_into_parts(full_name)
    surname = processed_player_name[0]
    given_name = processed_player_name[1]

    #coach is may not be constant between world cups. will have to change this, but ok for now
    processed_coach_name = process_name_into_parts(row[3])
    coach = processed_coach_name[1] + ' ' + processed_coach_name[0]

    if full_name not in players: #not sure there's any other way to distinguish?? but there has to be. there's probably at least a couple of John Smiths that have played
        player_id = len(players) + 1
        players[full_name] = [player_id, surname, given_name, coach]
        writer.writerow([player_id, surname, given_name, coach])


#helper function to deal with game events

def process_game_events(game_events_string):
    
    goals = []

    #for now, going to just deal with goals
    game_events_components = game_events_string.split(' ')

    for component in game_events_components:
        if 'G' in component:
            goals.append(component)

    return goals

def add_players_teams_matches_worldcups_entry(row, writer):

    #in order to check for repeated data (because there is some in the Kaggle dataset--that's why this is here
    already_added = set()



    player_full_name = row[6]
    team_abbreviation = row[2]

    match_id = row[1]

    wc_year = matches[match_id][0] #access the year via the matches dictionary, in order to get world_cup
    world_cup_id = world_cups[wc_year][0]

    player_id = players[player_full_name][0]
    team_id = teams[team_abbreviation][0]

    starter = ''
    captain = ''

    #is this useful?
    if row[4] == 'S':
        starter = 'Yes'
    else:
        starter = 'No'

    if row[7] == 'C':
        captain = 'Yes'
    else:
        captain = 'No'


    #just going to deal with goals right now
    goals = process_game_events(row[8])

    if len(goals) == 0:
        row_to_add = (player_id, team_id, match_id, world_cup_id, starter, captain, 'Null')
        if row_to_add not in already_added:
            writer.writerow(row_to_add)
            already_added.add(row_to_add)
    else:
        for goal in goals:
            row_to_add = (player_id, team_id, match_id, world_cup_id, starter, captain, goal)
            if row_to_add not in already_added:
                writer.writerow(row_to_add)
                already_added.add(row_to_add)

heading_row = next(world_cup_players_reader)
for row in world_cup_players_reader:

    add_player_entry(row, players_writer)
    add_players_teams_matches_worldcups_entry(row, players_teams_matches_worldcups_writer)

players_file.close()    
world_cup_players_data_file.close()
players_teams_matches_worldcups_file.close()


######################################################      
