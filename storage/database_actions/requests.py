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

#view a list of all storage
select_storage = generators.generate_select_query(
        "storage_storage"
)

#view a list 
select_inventory_from_storage = generators.generate_select_query(
    "storage_product",
    {   
        "storage_foldingaccounting":
        "storage_foldingaccounting.product_id=storage_product.id"
    },
    {
        "storage_storage":
        "storage_storage.id=storage_foldingaccounting.storage_id"
    },
)

select_incomming_and_outcomming = generators.generate_select_query(
    "storage_product",
    {
        "storage_incominginventoryset":
        "storage_incominginventoryset.product_id=storage_product.id"
    },
    {
        "storage_incominginvoices":
        "storage_incominginvoices.id=storage_incominginventoryset.incoming_invoices_id"
    },
    {
        "storage_outcominginventoryset":
        "storage_outcominginventoryset.product_id=storage_product.id"
    }
    {
        "storage_outcominginvoices":
        "storage_outcominginvoices.id=storage_outcominginventoryset.outncoming_invoices_id"
    }
)
