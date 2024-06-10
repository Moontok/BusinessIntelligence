import sqlite3

# Connect to the database
conn = sqlite3.connect('pizza_sales.db')

# Create a cursor object
cursor = conn.cursor()

# Update the data
cursor.execute(
    '''DELETE FROM sales WHERE id = 1;'''
)

# Commit the changes
conn.commit()

# Close the connection
conn.close()