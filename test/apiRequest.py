import requests
import json

# leer de un json local
#file = open("R2_D2.json", "r")
#data = json.load(file)
# print(data['name'])


# 6 tipos de busquedas: films, people,planets,species,starships,vehicles

#usar librerias complementarias  https://github.com/phalt/swapi-python
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
    item = response['results'][1]
    # for item in response['results']:
    #print(item['name'], len(item['films']))
    char = {
        'name': item['name'],
        'n_films': item['films'],
        'mass': item['mass'],
        "hair_color": item['hair_color'],
        "skin_color": item['skin_color'],
        "eye_color": item['eye_color'],
        "birth_year": item['birth_year'],
        "gender": item['gender'],
        "homeworld": item['homeworld'],
        "films": item['films'],
        "species": item['species'],
        "vehicles": item['vehicles'],
        "starships": item['starships'],
        'created': item['created'],
        "edited": item['edited'],
        "url": item['url']
    }
    charlist.append(char)
    return charlist


data = mainRequest(baseUrl, endpoint, 1)
my_json = json.dumps(parse_json(data), indent=4)
print(my_json)
outfile = open("ejemplo.json", "w")
outfile.write(my_json)
# for x in range(9):
#data = mainRequest(baseUrl, endpoint, x+1)
# parse_json(data)


# parse_json(data)
# print(parse_json(data))

#baseUrl = "http://rickandmortyapi.com/api"
#endPoint = 'character'
#r = requests.get(baseUrl+endpoint)
#data = r.json()
# listaResultados[15]=data['results'][0]
# print(data['results'][2])
