# KPI Sales Target Analysis
# This program calculates the average sales for a quarter and evaluates it against a KPI target.
# It demonstrates the use of functions.

# Function to evaluate data structures
def average_sales(sales_list):
    total_sales = 0
   
    # Loop to aggregate data
    for sale in sales_list:
        total_sales += sale
       
    # Calculate the average
    average_sales = total_sales / len(sales_list)

    return average_sales

# Data from Q1 sales performance
q1_sales = [12000, 15000, 11500]
kpi_target = 13000

# Executing the analytics function
q1_average = average_sales(q1_sales)
print(f"Quarterly Average Sales: ${q1_average:.2f}")

# Evaluating against KPI target
if q1_average >= kpi_target:
    print("KPI Target Met")
else:
    print("KPI Target Not Met")
