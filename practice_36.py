# Modify, normalize, mean-center, and sort NumPy array values
import numpy as np

salaries = np.array([25000, 45000, 70000, 38000, 92000, 55000, 48000, 31000, 67000, 84000])

salaries = salaries * 1.1

count = np.sum(salaries >= 50000) # Find how many employees earn above 50000

# — formula: (salary - min) / (max - min)
salaries = (salaries - np.min(salaries)) / (np.max(salaries) - np.min(salaries)) # Normalize the salaries between 0 and 1

salaries = salaries - np.mean(salaries)

salaries = np.sort(salaries)[::-1] # We want to sort from highest to lowest 

print(salaries)
# print(count)