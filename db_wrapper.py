import mysql.connector as connector


class DB:
    '''
        wrapper for getting the connection and cursor
        to the database
        @param host: host to connect to
        @param user: username for the connection
        @param db: database to connect to
        @param password: password for the connection
        @param port: port for the connection
        @returns: DB wrapper object
    '''

    def __init__(self, **kwargs):
        self.__host = 'localhost' if 'host' not in kwargs.keys() else kwargs.get('host')
        self.__user = 'root' if 'user' not in kwargs.keys() else kwargs.get('user')
        self.__db = 'redhat' if 'db' not in kwargs.keys() else kwargs.get('db')
        self.__password = 'example' if 'password' not in kwargs.keys() else kwargs.get('password')
        self.__port = 3306 if 'port' not in kwargs.keys() else kwargs.get('port')
        self.__con = connector.connect(
            user=self.__user,
            password=self.__password,
            port=self.__port,
            host=self.__host,
            database=self.__db
        )

    @property
    def con(self):
        return self.__con

    @property
    def cur(self):
        self.__cur = self.__con.cursor()
        return self.__cur

    def __del__(self):
        self.__con.commit()
        self.__con.close()
