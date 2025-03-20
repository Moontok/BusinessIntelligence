import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('pizza_sales.db')
cursor = conn.cursor()

# Calculate the unique types and their counts
response = cursor.execute(
    '''SELECT * FROM sales;'''
)

conn.commit()
conn.close()


