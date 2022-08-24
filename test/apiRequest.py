import requests
import json

# leer de un json local
#file = open("R2_D2.json", "r")
#data = json.load(file)
# print(data['name'])
baseUrl = "https://swapi.dev/api/"
endpoint = 'people/'


def mainRequest(baseURL, endpoint, x):
    r = requests.get(baseUrl+endpoint+f'?page={x}')
    return r.json()


def has_pages(response):
    if (response['next'] == 'null'):
        return False
    return true


def parse_json(response):
    charlist = []
    for item in response['results']:
        print(item['name'], len(item['films']))
        # char = {
        #    'name': item['name'],
        #    'n_films': item['films']
        # }
        # charlist.append(char)
    return  # charlist


data = mainRequest(baseUrl, endpoint, 1)
for x in range(9):
    data = mainRequest(baseUrl, endpoint, x+1)
    parse_json(data)


# parse_json(data)
# print(parse_json(data))

#baseUrl = "http://rickandmortyapi.com/api"
#endPoint = 'character'
#r = requests.get(baseUrl+endpoint)
#data = r.json()
# listaResultados[15]=data['results'][0]
# print(data['results'][2])
