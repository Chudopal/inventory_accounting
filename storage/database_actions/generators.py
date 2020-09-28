from storage.database_actions.database import Database
from psycopg2 import sql


DB = Database()
CURSOR = DB.connect()


def generate_insert_query(table_name: str, columns: list):
    """This functions allows to generate create-functions.
    This function is returning create-function for the concrete
    table.
    table_name - is a name of the table, which you want to update.
    columns - required columns in table.
    """
    def query(*values):
        """This function creates insert-queries to the database.
        values - is values you want to INSERT into the table.
        """
        values = list(values)        
        for item, _ in enumerate(values):
            if type(values[item]) == str:
                values[item] = "\'" + values[item] + "\'"
            values[item] = str(values[item])
        CURSOR.execute(
            sql.SQL(f"INSERT INTO {table_name}"\
                f"({', '.join(columns)}) VALUES ({', '.join(values)});")
        )
        print(f"INSERT INTO {table_name}"\
                f"({', '.join(columns)}) VALUES ({', '.join(values)});")

    return query


def generate_update_query(table_name: str):
    """This functions allows to generate update-functions
    This function is returning update-function for the concrete
    table.
    table_name - is a name of the table, which you want to update.
    """
    
    def query(column: str, value, id: int):
        """This function creates update-queries to the database. 
        column - is a column in a table, which you want to update,
        value - is a new value of selected columns,
        id - an identificator of a row:
            column = "a"
            value = "new"
            id = 10
        it equals:
            ...
            SET a = 'new'
            WHERE id = 10
            ...
         
        """
        if type(value) == str:
            value = "\'" + value + "\'"
        CURSOR.execute(
            sql.SQL(f"UPDATE {table_name}"\
                f" SET {column} = {value} WHERE id={id};")
        )

    return query


def generate_delete_query(table_name: str):
    """This functions allows to generate delete-functions
    This function is returning delete-function for the concrete
    table.
    table_name - is a name of the table, which you want to delete.
    """

    def query(id):
        """This function creates delete-queries to the database.
        id - is id in a table.
        """
        CURSOR.execute(
            sql.SQL(f"DELETE FROM {table_name} WHERE id={id};")
        )

    return query


def generate_select_query(*tables):
    """This is function allows to create select-functions.
    tables - is a list for tables and compositon of conditions:
        (
            "a",
            {"b": "b.a_id = a.id"},
            {"c": "b.c_id = c.id"},
        )
    It equals:
        ...
        a JOIN b 
        ON a.id = b.a_id
        JOIN c
        ON c.id = b.c_id
        ...
    """
    tables_join = tables[0]
    for table in tables[1:]:
        key = list(table.keys())[0]
        values = list(table.values())[0]
        tables_join += f" JOIN {key} ON {values} "

    def query(columns='*', conditions=[], order_by=""):
        """This function creates queries to the database.
        
        columns - is a list of columns in SLECT-query:
            columns = [
                "a", "b", "c",
            ]
        it equals:
            SELECT a, b, c FROM ...
        if list of columns is empty, the function 
        automatically selects all columns in a table(*)
        
        conditions - is a WHERE-sequence:
             conditions = [
                 "name='alex'",
                 "age>10",
             ]
        It equals:
            ...
            WHERE name = alex
            AND age > 10
            ...

        order_by - is ORDER BY in postgres:
            order_by = "a"
        It equals:
            ... 
            ORDER BY a
            ...
        """

        if not conditions:
            conditions_str = ""
        else:
            conditions_str = "WHERE " + " AND ".join(conditions)

        if order_by:
            if order_by[0] == "-":
                order_by_str = f"ORDER BY {order_by[1:]} "
                order_by_str += "DESK"
            else:
                order_by_str = f"ORDER BY {order_by}"
        else:
            order_by_str = ""

        CURSOR.execute(
            f"SELECT {', '.join(columns)}"\
            f" FROM {tables_join} {conditions_str} {order_by_str};"
        )
        print(
            f"SELECT {', '.join(columns)}"\
            f" FROM {tables_join} {conditions_str} {order_by_str};"
        )
        return CURSOR.fetchall()

    return query