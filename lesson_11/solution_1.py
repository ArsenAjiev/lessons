import sqlite3

# create a table products
def create_table():
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            amount INTEGER,
            comment TEXT); """)

        db.commit()


#create_table()


# add products in table
def create_products(name: str, price: float, amount: int, comment: str):
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        cursor.execute(
            """
            INSERT INTO products (name, price, amount, comment)
            VALUES( ?, ?, ?, ?);
            """,
            (name, price, amount, comment)
        )
        db.commit()

#ADD PRODUCTS

# create_products(name="Apple", price=2.50, amount=20, comment="fresh apple")
# create_products(name="Orange", price=1.50, amount=15, comment="fresh orange")
# create_products(name="Plump", price=3.50, amount=35, comment="fresh plump")
# create_products(name="Pear", price=6.50, amount=45, comment="fresh pear")
# create_products(name="watermelon", price=13.50, amount=35, comment="fresh watermelon")


# read products
def read_products():
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        cursor.execute(
            """ SELECT * FROM products; """, )
        db.commit()

    for result in cursor:
        print(result)


#read_products()

# update products, cherry insted of appple.
def update_products():
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        cursor.execute(
            """ UPDATE products
            SET name = 'cherry', comment = 'fresh cherry'
            WHERE id = 1;
            """, )
        db.commit()

#update_products()


# delete product, delete cherry where id == 1.
def delete_products():
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        cursor.execute(
            """ DELETE FROM products
            WHERE id = 1;
            """, )
        db.commit()

#delete_products()