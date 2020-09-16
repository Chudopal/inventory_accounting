import psycopg2
import os


class MetaSingleton(type):
    """Metaclass for creating singletone"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                MetaSingleton, cls
            ).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    """This class allows to connect to the database"""
    
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = psycopg2.connect(
                dbname=os.environ["DB_NAME"],
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASSWORD"],
                host=os.environ["HOST"]
            )
            self.cursor = self.connection.cursor()
        return self.cursor


DB = Database()
CURSOR = DB.connect()


CURSOR.execute('SELECT * FROM storage_product;')
records = CURSOR.fetchall()
print(records)