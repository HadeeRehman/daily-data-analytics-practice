# Analyze 2D sales array using axis sums, argmax, and argmin in NumPy
import numpy as np

sales = np.array([
    [200, 150, 300],
    [180, 220, 170],
    [250, 190, 210],
    [160, 300, 240]
])

print(sales.shape) # (rows, columns)
print(np.sum(sales, axis=0)) # Total sales per product — sum of each COLUMN
print(np.sum(sales, axis=1)) # Total sales per week — sum of each ROW
print(np.argmax(np.sum(sales, axis=0)))  # → 2 (Product 3 has highest total 920) / which column index has the highest total
print(np.argmin(np.sum(sales, axis=1))) # first do sum. Then the number column with lowest is given
