import csv
import json

with open("data.json") as jsonfile:
    data = json.load(jsonfile)

with open('data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    header = ["Title","url","Description"]
    csvwriter.writerow(header)
    for i in range(len(data)):
        dict = json.loads(data[i])

        title = dict.get("title", "No title available")
        url = dict.get("url", "No URL available")
        description = dict.get("description", "No description available")

        row = [title, url, description]

        csvwriter.writerow(row)

with open('data.csv', mode='r') as file:
    
    csv_reader = csv.DictReader(file)

    
    data_list = []

    
    for row in csv_reader:
        
        data_list.append(row)

for data in data_list:
    print(data)
    #extract data from here