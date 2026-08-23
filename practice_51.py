# Create and style a categorical bar chart using Matplotlib
import matplotlib.pyplot as plt
import numpy as np

categories = np.array(['Grains', 'Proteins', 'vegtables', 'fast food', 'healthy food'])

values = np.array([4, 6, 2, 8, 4])

plt.title('Daily consumpution', fontsize=10,
          fontweight='bold',
          family='Arial',
          color='green')
plt.xlabel('Food Items', fontsize=10,
           family='Arial',
           fontweight='bold',
           color='green')

plt.ylabel('Quantity', fontsize=10,
           family='Arial',
           fontweight='bold',
           color='green')

plt.bar(categories, values, color='red')
# plt.barh(categories, values, color='red') # For Horizontal Bar Graph

plt.show()