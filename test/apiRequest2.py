from select import select
from webbrowser import WindowsDefault
import requests
import json

# Modificar el codigo utilizando la libreria de la API https://github.com/phalt/swapi-python
# def mainRequest(baseURL, endpoint, x):
#    r = requests.get(baseUrl+endpoint+f'?page={x}')
#    return r.json()


def mainRequest(baseUrl, endpoint):
    r = requests.get(baseUrl+endpoint)
    return r.json()

#not used


# def has_pages(response):
#    if (response['next'] == 'null'):
#        return False
#    return true

#not used


# def parse_jsonPeople(response):
#    charlist = []
#    # for item in response['results']:
#    #print(item['name'], len(item['films']))
#    item = response
#   char = {
#        'name': item['name'],
#        'n_films': item['films'],
#        'mass': item['mass'],
#        "hair_color": item['hair_color'],
#       "skin_color": item['skin_color'],
#        "eye_color": item['eye_color'],
#        "birth_year": item['birth_year'],
#        "gender": item['gender'],
#        "homeworld": item['homeworld'],
#       "films": item['films'],
#        "species": item['species'],
#        "vehicles": item['vehicles'],
#        "starships": item['starships'],
#        'created': item['created'],
#       "edited": item['edited'],
#        "url": item['url']
#    }
#    charlist.append(char)
#    return charlist


def search(endpoint):
    data = mainRequest(baseUrl, endpoint)

    # return parse_json(data)
    return data


def printJson(data):
    nombreJson = input("Escriba el nombre del archivo:\n\n")
    my_json = json.dumps(data, indent=4)
    outfile = open(nombreJson+".json", "w")
    outfile.write(my_json)


def selectionPrint(resultadoBusqueda):
    selection = int(input("\nDesea imprimir 1-si    2_no\n"))
    if selection == 1:
        printJson(resultadoBusqueda)
    else:
        print("Tenga un buen dia :)")


def menuBusquedaID(endpoint):
    repetir = 1
    while (repetir == 1):

        busqueda = input("\nIngrese el n°ID ")
        resultadoBusqueda = search(endpoint+busqueda)
        if len(resultadoBusqueda) == 1:
            print(len(resultadoBusqueda))
            opcion = input(
                "ID no encontrado o valor desconocido, intentar otro ID?\n1_ Si    2_No\n")
            if opcion == '2':
                repetir = 0
        else:
            repetir = 0
    return resultadoBusqueda


def menuBusquedaSearch(endpoint):
    endpoint = endpoint+endpointSearch
    repetir = 1
    while (repetir == 1):

        busqueda = input("\nIngrese el nombre/titulo/modelo ")
        resultadoBusqueda = search(endpoint+busqueda)
        if len(resultadoBusqueda) == 1:
            print(len(resultadoBusqueda))
            opcion = input(
                "nombre/titulo/modelo no encontrado o valor desconocido, intentar otro?\n1_ Si    2_No\n")
            if opcion == '2':
                repetir = 0
        else:
            repetir = 0
    return resultadoBusqueda


def mainMenu():
    repetir = 1
    options = {
        1: 'films/',
        2: 'people/',
        3: 'planets/',
        4: 'species/',
        5: 'starships/',
        6: 'vehicles/'
    }
    while (repetir == 1):
        selection = int(input(
            "Bienvenido, Seleccione una opcion de busqueda \n1-films  2-people    3-planets   4-species   5-starships 6-vehicles\n"))
        if selection > 0 or selection <= 6:
            repetir = 0
        else:
            print("opcion incorrecta")

    endpoint = options[selection]

    selection = input(
        "1- Busqueda por id     2-Busqueda por nombre o modelo\n")
    # print(selection)

    if selection == '1':
        #print("dentro de opcion 1")
        resultadoBusqueda = menuBusquedaID(endpoint)
        print(resultadoBusqueda)
        selectionPrint(resultadoBusqueda)

    elif selection == '2':
        print("dentro de opcion 2")
        resultadoBusqueda = menuBusquedaSearch(endpoint)
        print(resultadoBusqueda)
        selectionPrint(resultadoBusqueda)


baseUrl = "https://swapi.dev/api/"
endpoint = ""
endpointSearch = '?search='

mainMenu()
