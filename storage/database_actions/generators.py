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
            sql.SQL(f"INSERT INTO {table_name}({', '.join(columns)}) VALUES ({', '.join(values)});")
        )

    return query


def generate_update_query(table_name: str):
    
    def query(column, value, id):
        if type(value) == str:
            value = "\'" + value + "\'"
        CURSOR.execute(
            sql.SQL(f"UPDATE {table_name} SET {column} = {value} WHERE id={id};")
        )

    return query


def generate_delete_query(table_name: str):

    def query(id):
        CURSOR.execute(
            sql.SQL(f"DELETE FROM {table_name} WHERE id={id};")
        )

    return query


def generate_select_query(tables: dict, conditions: dict):
    
    select_from = ""

    def query():
        pass

    return query