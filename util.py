import requests
import json
BASE_API = 'https://swapi.co/api/'
PEOPLES_API = BASE_API+'people/'
PEOPLE_API = BASE_API+'people/{}/'
FILMS_API = BASE_API+'films/{}/'


def get_all_people(id_list):
    heroes = []
    data = requests.get(PEOPLES_API).json()['results']
    # print(json.dumps(data, indent=4))
    for i in id_list:
        filtered_data = map(lambda y: dict(
            name=y['name'],
            films=y['films'],
            id=i), filter(lambda x: str(i) in x['url'],
                          data))
        heroes.extend(list(filtered_data))
    return json.dumps(heroes, indent=4)


def get_hero_info(id):
    data = requests.get(PEOPLE_API.format(id)).json()
    return dict(
        name=data['name'],
        films=data['films'],
        id=id
    )


def get_film_info(id):
    data = requests.get(FILMS_API.format(id)).json()
    return (id, data['title'])
