from database import Database


DB = Database()
CURSOR = DB.connect()


def add_product(name: str):
    CURSOR.execute(f"INSERT INTO storage_product(name) VALUES (\'{name}\');")


def select_product(quantity=0) -> list:
    if quantity == 0:
        CURSOR.execute(
            "SELECT * FROM storage_product;"
        )
    else:
        CURSOR.execute(
            f"SELECT * FROM storage_product LIMIT {quantity};"
        )
    return CURSOR.fetchall()


if __name__ == "__main__":
    add_product("Зонт")
    print(select_product())