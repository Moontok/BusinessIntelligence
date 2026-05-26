import sqlite3

def create_database():
    conn = sqlite3.connect('my_app.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL)
        );"""
    )
    conn.commit()
    conn.close()


def add_product(name, price):
    conn = sqlite3.connect('my_app.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO products (name, price)
        VALUES (?, ?);""", (name, price)
    )
    conn.commit()
    conn.close()