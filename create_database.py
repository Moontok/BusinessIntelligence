import sqlite3

# Create or connect to a database named pizza_sales.db
conn = sqlite3.connect('pizza_sales.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create a table named sales with columns: id, order_id, date, time, name, size, type, price
cursor.execute(
    '''CREATE TABLE sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        name TEXT NOT NULL,
        size TEXT NOT NULL,
        type TEXT NOT NULL,
        price REAL NOT NULL
    );'''
)

# Commit the changes
conn.commit()

# Close the connection
conn.close()