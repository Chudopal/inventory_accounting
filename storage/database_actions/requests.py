import generators

add_product = generators.generate_insert_query("storage_product", ["name"])
update_produt = generators.generate_update_query("storage_product")
delete_product = generators.generate_delete_query("storage_product")


if __name__ == "__main__":
    add_product("Веревка")
    update_produt("name","Меч", 20)
    delete_product(4)
    