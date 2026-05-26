import sqlite3

# Connect to the database
conn = sqlite3.connect('pizza_sales.db')

# Create a cursor object
cursor = conn.cursor()

# Select data from sales table
response = cursor.execute(
    '''SELECT * FROM sales;'''
)

# Fetch all the data
data = response.fetchall()

# Print the data
for row in data:
    print(row)

# Commit the changes
conn.commit()

# Close the connection
conn.close()