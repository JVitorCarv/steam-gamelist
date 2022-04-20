import json

with open('steamgames.json', 'r', encoding="utf8") as json_file:
    json_load = json.load(json_file)

gamelist = []
data = json_load['response']['games']
for game in data:
    gamelist.append(game['name'])

for name in gamelist:
    print(name)
