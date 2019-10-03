import os
import json
import copy
import pickle
import requests
from collections import defaultdict

# config variable used throughout the scripts

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_FILE = os.path.join(BASE_DIR, 'cache.pkl')
BASE_API = 'https://swapi.co/api/'
PEOPLES_API = BASE_API+'people/'
PEOPLE_API = BASE_API+'people/{}/'
FILMS_API = BASE_API+'films/{}/'


# black for caching the data
if os.path.exists(CACHE_FILE):
    obj = pickle.load(open(CACHE_FILE, 'rb'))
else:
    obj = dict(
        cache_characters=defaultdict(dict),
        cache_planets=defaultdict(dict),
        cache_starships=defaultdict(dict),
        cache_vehicles=defaultdict(dict),
        cache_species=defaultdict(dict),
        cache_film=defaultdict(dict),
        hero_info=defaultdict(dict),
        film_info=defaultdict(dict)
    )


def cache_obj():
    '''
        this pickles the caching object and 
        dumps it to a pickle file for future use
        everytime the object is altered 
        a new object is pickled and saved
    '''
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(obj, f)

# for processing data for films


def process_data(index, url):
    '''
        function to process the data
        fetch the data from the swapi
        removes the references and caches and returns clean object
        @param index: index corresponds to cache
        @param url: url to fetch or read from cache
        @returns: cleaned object
    '''
    lpop_map = dict(
        cache_characters=['homeworld', 'films',
                          'species', 'vehicles', 'starships', 'url'],
        cache_planets=['residents', 'films', 'url'],
        cache_starships=['films', 'url'],
        cache_vehicles=['pilots', 'films', 'url'],
        cache_species=['people', 'films', 'url']
    )
    data = obj.get(f'cache_{index}').get(url)
    if data:
        return copy.deepcopy(data)
    else:
        data = requests.get(url).json()
        lpop = lpop_map.get(f'cache_{index}')
        obj[f'cache_{index}'][url] = {i: j for i,
                                      j in data.items() if i not in lpop}
        return copy.deepcopy(obj[f'cache_{index}'][url])

# fetching data for hero


def get_hero_info(id):
    '''
        function to process the hero data
        fetch the data from the swapi
        removes the references and caches and returns clean object
        @param id: id to fetch or read from cache
        @returns: cleaned object
    '''
    data = obj.get('hero_info').get(id)
    if data:
        return copy.deepcopy(data)
    else:
        data = requests.get(PEOPLE_API.format(id)).json()
        obj['hero_info'][id] = dict(
            name=data['name'],
            films=data['films'],
            id=id
        )
        return copy.deepcopy(obj['hero_info'][id])

# fetching data for film


def get_film_info(id):
    '''
        function to process the film data
        fetch the data from the swapi
        removes the references and caches and returns clean object
        @param id: id to fetch or read from cache
        @returns: cleaned object
    '''
    data = obj.get('film_info').get('id')
    if data:
        return copy.deepcopy(data)
    else:
        data = requests.get(FILMS_API.format(id)).json()
        obj['film_info'][id] = (id, data['title'])
        return copy.deepcopy(obj['film_info'][id])

# fetching complete data for film


def get_film_complete_info(id):
    '''
        function to process the film data
        fetch the data from the swapi
        removes the references and caches and returns clean object
        @param id: id to fetch or read from cache
        @returns: cleaned object
    '''
    data = obj.get('cache_film').get(id)
    if data:
        return copy.deepcopy(data)
    else:
        data = requests.get(FILMS_API.format(id)).json()
        obj['cache_film'][id] = data
        return copy.deepcopy(obj['cache_film'][id])
