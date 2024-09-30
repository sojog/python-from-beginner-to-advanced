import csv
import json
from pprint import pp

with open("team.json", "r") as jsonfile:
    content = json.load(jsonfile)
    pp(content)


teams = []
with open("clwin.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for index, line in enumerate(reader):
        if index ==0:
            headers = line
        else:
            d = { headers[i]:line[i]  for i in range(len(line)) }
            teams.append(d)
            print(d)
            print(line)

with open("team.json", "w") as jsonfile:
    json.dump(teams, jsonfile)

