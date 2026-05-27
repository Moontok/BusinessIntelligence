import sqlite3


# Connect to the database
conn = sqlite3.connect('pizza_sales.db')

# Create a cursor object
cursor = conn.cursor()

# Select data at ID 1 from sales table
response = cursor.execute(
    '''SELECT * FROM sales WHERE id = 1;'''
)

# Fetch all the data
data = response.fetchall()

# Print the data
for row in data:
    print(row)

# Close the connection
conn.close()