import json, csv

with open ('logs.json', 'r') as file:
    data = json.load(file)
    print(data)
    with open ('error_logs.csv', 'w') as newFile:
        for item in data:
            print(item['level'])