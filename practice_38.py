# Conditionally categorize salaries and calculate bonuses using np.where()

import numpy as np

# np.where(condition, value_if_true, value_if_false)

salaries = np.array([25000, 45000, 70000, 38000, 92000, 55000, 48000, 31000, 67000, 84000])
ratings = np.array([3.5, 4.2, 4.8, 3.9, 4.6, 3.7, 4.1, 3.3, 4.5, 4.9])

level = np.where(salaries >=60000, "High", "Low")

bonus = np.where(ratings >= 4.5, salaries * 0.10, salaries * 0.05)

count =  np.sum(level == 'High')

print(count)