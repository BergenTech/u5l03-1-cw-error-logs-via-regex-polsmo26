import json, csv, re

with open ('logs.json', 'r') as file:
    data = json.load(file)
    # print(data)
    with open ('error_logs.csv', 'w', newline='') as newFile:
        writer = csv.DictWriter(newFile, fieldnames=data[0])
        writer.writeheader()
        pattern = r"^Error"
        for item in data:
            if re.search(pattern, item['message']):
                writer.writerows(data)
            else:
                pass