import generators

add_product = generators.generate_insert_query("storage_product", ["name"])



if __name__ == "__main__":
    add_product("Веревка")
    