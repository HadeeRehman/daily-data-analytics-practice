# Compare datasets with multi-class scatter plots and alpha styling
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) # Hourse Studied
y = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]) # Grades

x1 = np.array([0, 1, 1, 2, 2, 4, 5, 6, 7, 8, 8]) # Hourse Studied
y1 = np.array([55, 60, 60, 52, 68, 70, 75, 78, 82, 90, 97]) # Grades

plt.scatter(x, y, color='blue',
            alpha=0.5,
            s=100,
            label='Class A')
plt.scatter(x1, y1, color='red',
            alpha=1,
            s=100,
            label='Class B')

plt.xlabel('Hourse Studied', c='green')
plt.ylabel('Grade', c='green')
plt.title('Test Scores', c='green')
plt.legend()

plt.show()