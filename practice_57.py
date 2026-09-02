# Aggregate weekly coffee sales and visualize with a Seaborn heatmap

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

coffee_sales = pd.read_csv('Coffe_sales.csv')

day_totals = coffee_sales.groupby(['Weekday', 'Weekdaysort'])['money'].sum().reset_index().sort_values('Weekdaysort')

heatmap_data = day_totals['money'].values.reshape(1, -1)


plt.figure(figsize=(10, 2))

sns.heatmap(
    data=heatmap_data,
    cmap='Reds', 
    annot=True, 
    fmt=".0f", 
    xticklabels=day_totals['Weekday'],
    yticklabels=[]
)

plt.title("Total Spent By Day Of Week")
plt.xlabel('Day of Week')
plt.show()
