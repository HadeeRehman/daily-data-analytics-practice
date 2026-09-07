# Aggregate hourly coffee sales and plot line chart with Seaborn
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

coffee_sales = pd.read_csv('Coffe_sales.csv')

coffe_sales_by_hour = coffee_sales.groupby('hour_of_day')['money'].sum().reset_index() # grouped money under hours i.e money spent perhour


plt.figure(figsize=(8, 5))

sns.lineplot(
    data=coffe_sales_by_hour,
    x='hour_of_day',
    y='money',
    color='green',
    marker='.',
    ms=10,
)

plt.title('Coffee sales by hour')
plt.xlabel('Hours')
plt.ylabel('Total sales ($)')
plt.show()