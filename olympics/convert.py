#Written by Thea Traw

'''
Converts two olympics dataset csv files into separate csv files that will be used in my olympics database design.
'''

import csv

class FileParser:

    noc_dictionary = {}
    event_dictionary = {}
    unique_event_id = 1
    game_dictionary = {}
    unique_game_id = 1

    def read_file_into_lines(self, csv_file_name):
        data_file = open(csv_file_name, "r")
        lines_in_file = data_file.readlines()
        #data_file_length = len(lines_in_file)
        data_file.close()

        return lines_in_file

    def parse_noc_data(self):
        noc_regions = FileParser.read_file_into_lines(self, 'noc_regions.csv')
    
        nocs_table = []

        noc_unique_id = 1
        is_first_line = True
        for line in noc_regions:
            if is_first_line is False: #first line, not actual data
                row_for_table = FileParser.parse_line_noc_regions(line, noc_unique_id)
                nocs_table.append(row_for_table)
                noc_dictionary[row_for_table[0]] = row_for_table[1]
                noc_unique_id += 1
            else:
                is_first_line = False

        return nocs_table

    def parse_athlete_events_data(self):
        athlete_events = FileParser.read_file_into_lines(self, 'athlete_events.csv')

        athletes_table = []
        nocs_athletes_table = []
        athletes_medals_table = []
        games_table = []
        events_table = []
        medals_table = []

        is_first_line = True
        for line in athlete_events:
            if is_first_line is False:
           
                edited_data = FileParser.file_line_athlete_events(line)

                if edited_data[13] not in event_dictionary:
                    



            else:
                is_first_line = False

    def parse_line_noc_regions(line_in_data_file, noc_unique_id):
        all_line_data = line_in_data_file.split(',')
        row_for_table = [noc_unique_id, all_line_data[0], all_line_data[1]]
        return row_for_table
        

    def parse_line_athlete_events(line_in_data_file):
        all_line_data = line_in_data_file.split(',')
        
        full_name = all_line_data[1]
        name_split_index = full_name.rfind(' ')
        given_name = full_name[:name_split_index]
        surname = full_name[name_split_index + 1:]

        #all_line_data[0] is unique athlete id, [7] is noc, 
        edited_data = [all_line_data[0], surname, given_name, all_line_data[7], all_line_data[8], all_line_data[9], all_line_data[10], all_line_data[11], all_line_data[12], all_line_data[13], all_line_data[14]]
        
        return edited_line
    

    def parse_for_events_table(line_data):
        event_dictionary[line_data[13]] = unique_event_id
        unique_event_id += 1
        row_for_table = [unique_event_id, line_data[13], line[12]]
        return row_for_table

    def parse_for_games(line_data):
        game_dictionary[line_data[8]] = unique_game_id
        unique_game_id += 1
        row_for_table = [unique_game_id, line_data[9], line_data[10], line_data[11]]
        return row_for_table
        
    def parse_for_athletes_table(line_data):
        row_for_table = [line_data[0], line_data[1], line_data[2], noc_dictionary[line_data[3]], event_dictionary[line_data[9]], game_dictionary[line_data[4]], line_data[10]]

    def parse_for_medals_table(line_data, unique_medal_id):
        row_for_table = [unique_medal_id, line_data[10], game_dictionary[line_data[4]], event_dictionary[line_data[9]], line_data[0]]

    
    def write_file(table):
        with open('/Users/theat/Downloads/nocs.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(table)

def main():
    file_parser = FileParser()
    nocs_table = file_parser.parse_noc_data()
    FileParser.write_file(nocs_table)
    

if __name__ == '__main__':
    main()
