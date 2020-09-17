from database import Database
from psycopg2 import sql

DB = Database()
CURSOR = DB.connect()


def generate_insert_query(table_name: str, columns: list):

    def query(*values):
        values = list(values)        
        for item, _ in enumerate(values):
            if type(values[item]) == str:
                values[item] = "\'" + values[item] + "\'"
            values[item] = str(values[item])
        CURSOR.execute(
            sql.SQL(f"INSERT INTO {table_name}({','.join(columns)}) VALUES ({', '.join(values)});")
        )

    return query
