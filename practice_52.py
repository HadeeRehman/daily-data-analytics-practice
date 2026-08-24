# Create a customized pie chart with dynamic explode and shadow effects
import matplotlib.pyplot as plt
import numpy as np

categories = np.array(['Freshman', 'junior', 'senior', 'sophomores'])
values = np.array([300, 200, 340, 270])

explode = [0] * len(values)
explode[1] = 0.1 # here We use index inside the explode

colors = ['red', 'green', 'purple', 'gray']

plt.pie(values, labels=categories, 
        autopct='%1.1f%%',
        colors=colors,
        # explode=[0, 0, 0, 0.1],
        explode=explode, # Another way
        shadow=True,
        startangle=90)

plt.title('Radiant Public')

plt.show()