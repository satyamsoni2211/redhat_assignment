import mysql.connector as connector
from db_wrapper import DB

db = DB(db=None)
cur = db.cur
print('creating database')
cur.execute('create database redhat')
cur.execute('use redhat')
print('Creating tables')
cur.execute('drop table if exists hero, film, films, map')
cur.execute('''
create table hero (
    id int not null,
    name varchar(100) not null,
    unique key(id,name)
)
''')
cur.execute('''
create table films (
    id int not null,
    name varchar(100) not null,
    unique key(id,name)
)
''')
cur.execute('''
create table map (
    hero_id int not null,
    film_id int not null,
    unique key(hero_id,film_id)
)
''')
cur.execute('show tables')
print(cur.fetchall())
