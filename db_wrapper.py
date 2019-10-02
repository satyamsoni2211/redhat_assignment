import mysql.connector as connector


class DB:
    def __init__(self, **kwargs):
        self.__host = 'localhost' if 'host' not in kwargs.keys() else kwargs.get('host')
        self.__user = 'root' if 'user' not in kwargs.keys() else kwargs.get('user')
        self.__db = 'redhat' if 'db' not in kwargs.keys() else kwargs.get('db')
        self.__password = 'example' if 'password' not in kwargs.keys() else kwargs.get('password')
        self.__port = 3306 if 'port' not in kwargs.keys() else kwargs.get('port')
        self.__con = connector.connect(
            user='root',
            password='example',
            port=3306,
            host='localhost',
            database='redhat'
        )

    @property
    def con(self):
        return self.__con

    @property
    def cur(self):
        self.__cur = self.__con.cursor()
        return self.__cur

    def create_tables(self):
        cur = self.cur
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

    def __del__(self):
        self.__con.commit()
        self.__con.close()
