# Plot monthly revenue trends using a line chart in Matplotlib

import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [12000, 15000, 13500, 18000, 22000, 19500, 25000, 27000, 24000, 29000, 32000, 35000]


plt.plot(months, revenue, marker='o',
         markersize=10,
         markerfacecolor='red')

plt.grid(True)
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Monthly Revenue - 2024')
plt.show()