# Plot mean departmental salary using Seaborn barplot
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'dept': ['Sales', 'Sales', 'IT', 'IT', 'HR', 'HR', 'Sales', 'IT', 'HR', 'Sales'],
    'salary': [50000, 55000, 70000, 80000, 48000, 52000, 60000, 90000, 51000, 45000],
    'rating': [4.5, 4.9, 3.8, 4.2, 4.1, 3.9, 4.6, 4.7, 4.3, 3.5]
})
sns.barplot(
    data=data,
    x='dept',
    y='salary',
    hue='dept',
    palette='Set1',
    legend=False,
)
plt.show()