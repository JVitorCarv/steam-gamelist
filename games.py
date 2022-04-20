from urllib.request import urlopen
import json

key = input('Inform your API key: ')
id = input('Inform your steam ID: ')

url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={id}&format=json&include_appinfo=true&include_played_free_games=true'

response = urlopen(url)

json_load = json.loads(response.read())

gamelist = []
count = json_load['response']['game_count']
data = json_load['response']['games']
for game in data:
    gamelist.append(game['name'])

gamelist.sort()
for name in gamelist:
    print(name)

print(f'\nTotal: {count}')

answer = ''
print('Do you wish to save your games in a txt file? Y/N')
while(answer != 'Y' and answer != 'N'):
    answer = input()
    answer = answer.upper()


if answer == 'Y':
    with open('list_of_games.txt', 'w+', encoding='utf-8') as file:
        for name in gamelist:
            file.write(f'{name}\n')
        file.write(f'\nTotal games: {count}')
        print('File saved')

print('Good bye')
