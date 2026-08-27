# Generate clipped normal distribution and plot score histogram
import numpy as np
import matplotlib.pyplot as plt

score = np.random.normal(loc=80, scale=10, size=100)

score = np.clip(score, 0, 100)


plt.hist(score, bins=10, 
         color='green',
         edgecolor='black')

plt.title('Exam Scores')
plt.xlabel('Score')
plt.ylabel('Number Of Student')

plt.yticks()

plt.show()
