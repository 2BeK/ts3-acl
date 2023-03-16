import csv, json, re, argparse
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
                  'VICTOR','WHISKEY','X-RAY','XRAY','YANKEE','ZULU',\
                  'ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINER','NINE']
			
## Create the parser
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--csv_export', action='store_true', help='create CSV export of airlines')  # CSV export on/off flag
parser.add_argument('-j', '--json_export', action='store_true', help='create JSON export of airlines')  # JSON export on/off flag
args = parser.parse_args()

## Get game path
print("Paste game path (e.g. C:\SteamLibrary\steamapps\common\Tower! Simulator 3):")
game_path: Path = Path(input())
print("Your game path is set to \"{}\"".format(game_path))

print(game_path)
#airplanes_path = game_path / 'Airplanes'
airports_path = game_path / 'Airports'

#print(airplanes_path)
#print(airports_path)

## Iterate through all airport folders (e.g. KLAX, KLGA, ...)
for airport_path in airports_path.iterdir():
    
    if airport_path.is_dir():
        print("[i] Parse {}".format(airport_path.name))
        databases_path = airport_path / 'databases'
        
        ## Iterate through all database folders (e.g. default, NyergesDesign, ...)
        for database_path in databases_path.iterdir():
            
            if database_path.is_dir():
                print("[i]\t Found {} database".format(database_path.name))
                list_of_unique_callsigns_per_schedule = []
                callsign_table = []
                #callsign_table.append(['Airline', 'Callsign', 'Name', 'Country Code'])
                
                ## Open schedule and create a dict/list of airlines that are active in particular airport
                schedule_file = database_path / 'schedule.csv'
                with open(schedule_file) as csv_file:
                    csv_reader_object = csv.DictReader(csv_file)
                    
                    for row in csv_reader_object:
                        if row['airline (callsign)'] not in list_of_unique_callsigns_per_schedule:
                            list_of_unique_callsigns_per_schedule.append(row['airline (callsign)'])
                
                ## Open airlines and save only airlines that are active on particular airport as per schedule
                airlines_path = database_path / 'airlines.csv'
                with open(airlines_path) as csv_file:
                    csv_reader_object = csv.DictReader(csv_file)
                    
                    for row in csv_reader_object:
                        if row['Airline'] in list_of_unique_callsigns_per_schedule:
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
                
                ####################
                # Create CSV files #
                ####################
                
                ## Check if CSV folder is available
                csv_path: Path = Path('csv')
                if not csv_path.is_dir():
                    csv_path.mkdir()
                
                file_name = "csv/{}_{}.csv".format(airport_path.name, database_path.name)
                
                with open( file_name, 'w', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(['Airline', 'Callsign', 'Name', 'Country Code'])
                    
                    for airline in sorted_callsign_table:
                        #print(airline)
                        writer.writerow(airline)
                
                #####################
                # Create JSON files #
                #####################
                
                ## Check if JSON folder is available
                json_path: Path = Path('json')
                if not json_path.is_dir():
                    json_path.mkdir()
                
                json_string = ""
                
                for row in sorted_callsign_table:
                    airline_json = {"Airline": row[0],\
                                    "Callsign": row[1],\
                                    "Name": row[2],\
                                    "Country Code": row[3]}
                    json_string += json.dumps(airline_json, indent=4) + "\n"
                
                file_name = "json/{}_{}.json".format(airport_path.name, database_path.name)
                
                with open( file_name, 'w') as json_file:
                    json_file.write(json_string)
print("[i] Finished!")