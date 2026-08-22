# Customize plot titles, axis labels, font properties, and tick parameters
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2002, 2003, 2004, 2005])
y1 = np.array([10, 30, 28, 20])
y2 = np.array([17, 26, 38, 7])
y3 = np.array([23, 55, 10, 19])

plt.title('Class Size', fontsize=20,
        family='Arial',
        fontweight='bold',
        color='blue')

plt.xlabel('Year', fontsize=20,
           family='Arial',
           fontweight='bold',
           color='green')

plt.ylabel('Students', fontsize=20,
           family='Arial',
           fontweight='bold',
           color='brown')

plt.tick_params(axis='both',
        colors='black')

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)



plt.show()