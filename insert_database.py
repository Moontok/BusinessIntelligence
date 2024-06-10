import sqlite3

# Connect to the database
conn = sqlite3.connect('pizza_sales.db')

# Create a cursor object
cursor = conn.cursor()

# Insert data into the sales table
cursor.execute(
    '''INSERT INTO sales (order_id, date, time, name, size, type, price)
        VALUES ('2015-000001', '1/1/2015', '11:38:36', 'hawaiian', 'L', 'classic', 13.25
    );'''
)

# Commit the changes
conn.commit()

# Close the connection
conn.close()