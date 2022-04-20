import json

with open('steamgames.json', 'r', encoding="utf8") as json_file:
    json_load = json.load(json_file)

data = json_load['response']['games']
for game in data:
    print(game['name'])
