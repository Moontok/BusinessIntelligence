import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect('pizza_sales.db')

# Create a cursor object
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

# Read the CSV file
with open('pizza_sales.csv', 'r') as file:
    reader = csv.reader(file)
    h = next(reader)

    for row in reader:
        cursor.execute(
            '''INSERT INTO sales (order_id, date, time, name, size, type, price)
            VALUES (?, ?, ?, ?, ?, ?, ?);''', row[1:]          
        )

# Commit the changes
conn.commit()

# Close the connection
conn.close()