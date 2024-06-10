import sqlite3

# Connect to the database
conn = sqlite3.connect('pizza_sales.db')
cursor = conn.cursor()

# Get Data from the database
response = cursor.execute(
    '''SELECT * FROM sales;'''
)
data = response.fetchall()

conn.commit()
conn.close()

print(data[0])

# Count the number of sales using Python
print("Number of sales:", len(data))

# Calculate the total sales using Python
total_sales = 0
for row in data:
    total_sales += row[7]
print("Total sales:", total_sales)

# Calculate the average sales using Python
average_sales = total_sales / len(data)
print("Average sales:", average_sales)

# Calculate the maximum sales using Python
max_sales = 0
for row in data:
    if row[7] > max_sales:
        max_sales = row[7]
print("Maximum sales:", max_sales)

# Calculate the minimum sales using Python
min_sales = max_sales
for row in data:
    if row[7] < min_sales:
        min_sales = row[7]
print("Minimum sales:", min_sales)


import matplotlib.pyplot as plt


types = {}
for row in data:
    if row[6] in types:
        types[row[6]] += 1
    else:
        types[row[6]] = 1
print(types)

plt.pie(types.values(), labels=types.keys(), autopct='%1.1f%%')
plt.axis('equal')
plt.show()
