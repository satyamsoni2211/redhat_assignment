import json
import requests
from db_wrapper import DB
from random import randint
from collections import defaultdict
from util import get_hero_info, get_film_info, obj, cache_obj

db = DB()
con = db.con
cur = db.cur
rdata = defaultdict(list)

data = [get_hero_info(i)
        for i in map(lambda x: randint(1, 87), range(15))]

# processing hero_data
hero_data = dict([(i['id'], i['name']) for i in data])
cur.executemany('''
    insert ignore into hero (id, name) values (%s,%s)
    ''', hero_data.items())
print(cur.rowcount, 'inserted')

# processing hero_film_mapping
hero_film_mapping = [(i['id'], j.split('/')[-2])
                     for i in data for j in i['films']]
cur.executemany('''
    insert ignore into map (hero_id, film_id) values (%s,%s)
    ''', hero_film_mapping)
print(cur.rowcount, 'inserted')

# processing film_data
film_data = dict([get_film_info(i[1]) for i in hero_film_mapping])
cur.executemany('''
    insert ignore into films (id, name) values (%s,%s)
    ''', film_data.items())
print(cur.rowcount, 'inserted')

for i in hero_film_mapping:
    rdata[film_data[i[1]]].append(hero_data[i[0]])
print(json.dumps(rdata, indent=4))

# caching
cache_obj()
