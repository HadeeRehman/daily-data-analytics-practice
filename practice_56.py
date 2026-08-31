# Plot horizontal bar chart for categorical value counts using Pandas and Matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')

plt.figure(figsize=(8, 5))

type_layout = df['Type1'].value_counts(ascending=True)

plt.barh(type_layout.index, type_layout.values, color='green',
        edgecolor='black')
plt.title('Pokemon Type1 Distribution', color='purple', fontweight='bold')
plt.xlabel('Highest Ability', color='blue')
plt.ylabel('Abilities', color='green')

plt.tight_layout()
plt.show()