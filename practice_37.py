# Analyze multi-month product sales performance and consistency in NumPy
import numpy as np

# Monthly sales for 3 products over 6 months
sales = np.array([
    [120, 85, 200],
    [135, 90, 180],
    [150, 78, 220],
    [110, 95, 195],
    [160, 88, 210],
    [145, 92, 205]
])
# rows = months, columns = products

product = np.argmax(np.mean(sales, axis=0)) + 1

highest_sales = np.argmax(np.sum(sales, axis=1)) + 1

count = np.sum(sales[:, 0] > np.mean(sales[:, 0])) # Compare every value with the average

product_total = np.sum(sales, axis=0) # total per product (sum each column)

grand_total = np.sum(product_total) #  grand total (sum everything)

percentage = (product_total / grand_total) * 100

consistent_sales = np.argmin(np.std(sales, axis=0)) + 1

# print(product)
# print(highest_sales)
# print(count)
print(percentage)
# print(consistent_sales)

