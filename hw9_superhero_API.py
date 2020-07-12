import requests
superhero_list = ['Hulk', 'Captain America', 'Thanos']
count = 0
output = []
for name in superhero_list:
    response  = requests.get(f'https://www.superheroapi.com/api.php//search/{name}')
    intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
    if intelligence > count:
        count = intelligence
        output = [name, count]
print(f'самый умный {output[0]}, уровень "intelligence" - {output[1]}')
