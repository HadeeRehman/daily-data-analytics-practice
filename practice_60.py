# Create clustered bar chart of transactions by time of day using Seaborn
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


coffe_sales = pd.read_csv('Coffe_sales.csv')

coffe_sales["trasaction_count"] = 1 
plt.figure(figsize=(8, 5))

sns.barplot(
    data=coffe_sales,
    x="Time_of_Day",
    y="trasaction_count",
    hue='coffee_name', 
    estimator='sum',   
    palette='Set1'
)
plt.title('Number of Trasactions by time of day', fontsize=14)
plt.xlabel('Afternoon')
plt.ylabel('Trascation count')
plt.legend()
plt.show()