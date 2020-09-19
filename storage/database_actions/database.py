import psycopg2
import os


class MetaSingleton(type):
    """Metaclass for creating singletones"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                MetaSingleton, cls
            ).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    """This class allows to connect to the database.
    For connecting to the database you must 
    define environment variables:
        DB_NAME - database's name 
        DB_USER - user name
        DB_PASSWORD - database's password
        HOST - host of database
    """

    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = psycopg2.connect(
                dbname=os.environ["DB_NAME"],
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASSWORD"],
                host=os.environ["HOST"]
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        return self.cursor