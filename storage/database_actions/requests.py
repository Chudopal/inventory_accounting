import generators
from database import Database
from psycopg2 import sql

#queries for product
add_product = generators.generate_insert_query(
    "storage_product", ["name"]
)
update_product = generators.generate_update_query(
    "storage_product"
)
delete_product = generators.generate_delete_query(
    "storage_product"
)

#queries for storage
add_storage = generators.generate_insert_query(
    "storage_storage", ["name", "phone_number"]
)
update_storage = generators.generate_update_query(
    "storage_storage"
)
delete_storage = generators.generate_delete_query(
    "storage_storage"
)

#queries for incomming invoices
add_incomming_invoices = generators.generate_insert_query(
    "storage_incomminginvoices", 
    ["storage_id", "date", "name", "position"]
)
update_incomming_invoices = generators.generate_update_query(
    "storage_incomminginvoices"
)
delete_incomming_invoices = generators.generate_delete_query(
    "storage_incomminginvoices"
)

#queries for incomming inventory set
add_incomming_inventory_set = generators.generate_insert_query(
    "storage_incominginventoryset",
    ["incoming_invoices_id", "product_id", "quantity"]
)
update_incomming_inventory_set = generators.generate_update_query(
    "storage_incominginventoryset"
)
delete_incomming_inventory_set = generators.generate_delete_query(
    "storage_incominginventoryset"
)

#queries for outcomming invoices
add_outcomming_invoices = generators.generate_insert_query(
    "storage_outcomminginvoices", 
    ["storage_id", "date", "name", "position"]
)
update_outcomming_invoices = generators.generate_update_query(
    "storage_outcomminginvoices"
)
delete_outcomming_invoices = generators.generate_delete_query(
    "storage_outcomminginvoices"
)

#queries for outcomming inventory set
add_outcomming_inventory_set = generators.generate_insert_query(
    "storage_outcominginventoryset",
    ["outcoming_invoices_id", "product_id", "quantity"]
)
update_outcomming_inventory_set = generators.generate_update_query(
    "storage_outcominginventoryset"
)
delete_outcomming_inventory_set = generators.generate_delete_query(
    "storage_outcominginventoryset"
)

#queries for folding accounting
add_folding_accounting = generators.generate_insert_query(
    "storage_foldingaccounting",
    ["storage_id", "product_id", "incomming", "outcomming"]
)
update_folding_accounting = generators.generate_update_query(
    "storage_foldingaccounting"
)
delete_folding_accounting = generators.generate_delete_query(
    "storage_foldingaccounting"
)

DB = Database()
CURSOR = DB.connect()


def select_inventory_in_storage(product, storage):
    CURSOR.execute(
        f"""SELECT sp.product, sf.incomming, sf.outcomming FROM storage_product sp
        JOIN storage_foldingaccounting sf
        ON sp.id = sf.product_id
        JOIN storage_storage ss
        ON ss.id = sp.storage_id
        WHERE ss.name = {storage}
        AND sp.name = {product};
        """
    )


def select_incomming_and_outcomming(product):
    CURSOR.execute(
        f"""SELECT sp.name, so.date, si_set.quantity, so.date, so_set.quantity FROM storage_product sp
        JOIN storage_incominginventoryset si_set
        ON si_set.product_id = sp.id
        JOIN storage_incominginvoices si
        ON si_set.incoming_invoices_id = si.id
        JOIN storage_outcominginventoryset so_set
        ON so_set.product_id = sp.id
        JOIN storage_outcominginvoices so
        ON so_set.outncoming_invoices_id = so.id
        WHERE sp.name = {product};
        """
    )


def select_storages():
    CURSOR.execute(
        f"""SELECT number, name, phone_number FROM storage_storage ss"""
    )


if __name__ == "__main__":
    add_product("Веревка")
    update_product("name","Меч", 20)
    delete_product(4)
    