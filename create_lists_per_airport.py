import csv, re
from pathlib import Path

# ask for game path
# open airports folder
#   give option which folder to work through (airport/all)
#   save option and (first) airport
# open databases folder
#   give option which folder to work through (default/NyergesDesign/all)
#   save selection for other folders if "all" is chosen in first question
# open schedule and create a dict/list of airlines
# open airlines and save all airlines that have active schedule entries
# create json/csv/excel/pdf file

exclusion_list = ['APLHA','BRAVO','CHARLIE','DELTA','ECHO','FOXTROT','GOLF',\
                  'HOTEL','INDIA','JULIET','KILO','LIMA','MIKE','NOVEMBER',\
                  'OSCAR','PAPA','QUEBEC','ROMEO','SIERRA','TANGO','UNIFORM',\
                  'VICTOR','WHISKEY','X-RAY','YANKEE','ZULU',\
                  'ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINER','NINE']
			


print("Paste game path (e.g. C:\SteamLibrary\steamapps\common\Tower! Simulator 3):")
#game_path = input()
game_path: Path = Path(input())

## Get game path
print("Your game path is set to \"{}\"".format(game_path))

print(game_path)
#airplanes_path = game_path / 'Airplanes'
airports_path = game_path / 'Airports'

#print(airplanes_path)
print(airports_path)

## Iterate through all airport folders (e.g. KLAX, KLGA, ...)
for airport_path in airports_path.iterdir():
    if airport_path.is_dir():
        print(airport_path.name)
        databases_path = airport_path / 'databases'
        #print(databases_path)
        
        ## Iterate through all database folders (e.g. default, NyergesDesign, ...)
        for database_path in databases_path.iterdir():
            if database_path.is_dir():
                print(database_path.name)
                list_of_unique_callsigns_per_schedule = []
                callsign_table = []
                #callsign_table.append(['Airline', 'Callsign', 'Name', 'Country Code'])
                
                file_name = "{}_{}.csv".format(airport_path.name, database_path.name)
                with open( file_name, 'w', newline='') as csvfile:
                    #fieldnames = ['Airline', 'Callsign', 'Name', 'Country code']
                    #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    #writer.writeheader()
                    writer = csv.writer(csvfile)
                
                    ## Open schedule and create a dict/list of airlines that are active in particular airport
                    schedule_file = database_path / 'schedule.csv'
                    with open(schedule_file) as csv_file:
                        csv_reader_object = csv.DictReader(csv_file)
                        for row in csv_reader_object:
                            #print(row['airline (callsign)'])
                            if row['airline (callsign)'] not in list_of_unique_callsigns_per_schedule:
                                list_of_unique_callsigns_per_schedule.append(row['airline (callsign)'])
                    ##print(list_of_unique_callsigns_per_schedule)
                    
                    ## Open airlines and save only airlines that are active on particular airport as per schedule
                    airlines_path = database_path / 'airlines.csv'
                    with open(airlines_path) as csv_file:
                        csv_reader_object = csv.DictReader(csv_file)
                        
                        for row in csv_reader_object:
                            if row['Airline'] in list_of_unique_callsigns_per_schedule:
                                ##print(row)
                                #writer.writerow(row)#############################################
                                callsign_table.append([row['Airline'],\
                                                      row['Callsign'],\
                                                      row['Name'],\
                                                      row['Country code']])
                    
                    ga_path = database_path / 'ga.csv'
                    re_list_callsign_say = r'\b(ZERO|ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINER|NINE)\b'
                    
                    with open(ga_path) as csv_file:
                        csv_reader_object = csv.DictReader(csv_file)
                        for row in csv_reader_object:
                            #print("{} - {}".format(row['callsign say'], re.split(re_list_callsign_say, row['callsign say'], maxsplit=1)))
                            #print("{}".format(row['callsign say']))
                            if  row['callsign say'].strip().split(' ')[0].upper() not in exclusion_list and\
                                not any(re.split(r'\d', row['callsign'].upper())[0].lstrip(' ') in airline for airline in callsign_table):
                                #print("{}".format(row['callsign say'].split(' ')))
                                #print("{}".format(re.split(re_list_callsign_say, row['callsign say'].upper())[0]))
                                #print("{}".format(re.split(r'\d', row['callsign'].upper())))
                                callsign_table.append([re.split(r'\d', row['callsign'].upper())[0].strip(),\
                                                       re.split(re_list_callsign_say, row['callsign say'].upper())[0].strip(),\
                                                       '',\
                                                       'GA'])
                    
                    sorted_callsign_table = sorted(callsign_table, key=lambda x: x[0])
                    #print(callsign_table)
                    #print(sorted_callsign_table)
                    
                    writer.writerow(['Airline', 'Callsign', 'Name', 'Country Code'])
                    for airline in sorted_callsign_table:
                        print(airline)
                        writer.writerow(airline)