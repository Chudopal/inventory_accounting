import generators
from database import Database
from psycopg2 import sql

add_product = generators.generate_insert_query("storage_product", ["name"])
update_produt = generators.generate_update_query("storage_product")
delete_product = generators.generate_delete_query("storage_product")


DB = Database()
CURSOR = DB.connect()


def select_inventory_in_storage(product, storage):
    CURSOR.execute(
        f"""SELECT * FROM storage_product sp
        JOIN storage_foldingaccounting sf
        ON sp.id = sf.product_id
        JOIN storage_storage ss
        ON ss.id = sp.storage_id
        WHERE ss.name = {storage}
        AND sp.name = {product};
        """
    )


def select_incomming_and_outcomming():
    CURSOR.execute(
        f"""SELECT * FROM 
        """
    )


def select_storages():
    pass


if __name__ == "__main__":
    add_product("Веревка")
    update_produt("name","Меч", 20)
    delete_product(4)
    