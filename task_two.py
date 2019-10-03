import os
import json
import pickle
import requests
from db_wrapper import DB
from util import get_film_complete_info, process_data, obj, CACHE_FILE, cache_obj

# fetching connection
db = DB()
con = db.con
cur = db.cur


# fetching data for movie
cur.execute('select * from films where name like "%{}%"'.format('A New Hope'))
res = cur.fetchall()
data = get_film_complete_info(1) if not len(
    res) else get_film_complete_info(res[0][0])

# processing data
data['characters'] = [process_data('characters', i)
                      for i in data['characters']]
data['planets'] = [process_data('planets', i) for i in data['planets']]
data['starships'] = [process_data(
    'starships', i) for i in data['starships']]
data['vehicles'] = [process_data('vehicles', i) for i in data['vehicles']]
data['species'] = [process_data('species', i) for i in data['species']]

# composing json file
with open('task_two.json', 'w') as js:
    json.dump(data, js, indent=4)

# pickling the cache object
cache_obj()
