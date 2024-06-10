import sqlite3

# Connect to the database
conn = sqlite3.connect('pizza_sales.db')
cursor = conn.cursor()

# Calculate the total sales using the SUM() function in SQL
# response = cursor.execute(
#     '''SELECT SUM(price) FROM sales;'''
# )
# total_sales = response.fetchone()[0]
# total_sales = round(total_sales, 2)
# print(f'Total sales: ${total_sales}')

# Calculate the total sales using Python
response = cursor.execute(
    '''SELECT price FROM sales;'''
)
data = response.fetchall()
total_sales = 0
for row in data:
    total_sales += row[0]
total_sales = round(total_sales, 2)
print(f'Total sales: ${total_sales}')

# Calculate the average sales using Python
average_sales = total_sales / len(data)
average_sales = round(average_sales, 2)
print(f'Average sales: ${average_sales}')

# Calculate the maximum sales using Python
max_sale = 0
for row in data:
    if row[0] > max_sale:
        max_sale = row[0]
max_sale = round(max_sale, 2)
print(f'Maximum sale: ${max_sale}')

# Calculate the minimum sales using Python
min_sale = max_sale
for row in data:
    if row[0] < min_sale:
        min_sale = row[0]
min_sale = round(min_sale, 2)
print(f'Minimum sale: ${min_sale}')

conn.commit()
conn.close()


