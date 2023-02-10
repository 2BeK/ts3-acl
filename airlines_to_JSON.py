import csv, json

with open("airlines.csv") as csvdatei:
    csv_reader_object = csv.DictReader(csvdatei)
    json_string = ""
    
    for row in csv_reader_object:
        json_string += json.dumps(row, indent=4) + "\n"
    
    print(json_string)
    
    f = open("airlines.json", "w")
    f.write(json_string)
    f.close()
