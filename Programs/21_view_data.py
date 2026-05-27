import sqlite3
import matplotlib.pyplot as plt


# Connect to the database
conn = sqlite3.connect('pizza_sales.db')
cursor = conn.cursor()

# Get Data from the database
response = cursor.execute(
    '''SELECT * FROM sales;'''
)
data = response.fetchall()

conn.close()

# Process the data to get the count of each pizza type
types = {}
for row in data:
    if row[6] in types:
        types[row[6]] += 1
    else:
        types[row[6]] = 1
print(types)

# Create a pie chart to show the distribution of pizza types
plt.pie(types.values(), labels=types.keys(), autopct='%1.1f%%')
plt.title('Distribution of Pizza Types')
plt.axis('equal') # Equal aspect ratio ensures that pie chart is circular.
plt.show()