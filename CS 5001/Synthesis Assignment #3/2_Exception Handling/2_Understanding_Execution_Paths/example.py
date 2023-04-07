# Michael Arthur Mills
# April 7. 2023
# CS 5001

# An example of recursion

sales_list = [100, 150, 200, 175, 225, 250, 300]

def calculate_sales(sales_list):
    if len(sales_list) == 0:
        return 0
    else:
        return sales_list[0] + calculate_sales(sales_list[1:])
    
total_sales = calculate_sales(sales_list)
print(total_sales)