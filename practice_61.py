# Plot salary distribution with KDE curve using Seaborn histplot
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.DataFrame({
    'dept': ['Sales', 'Sales', 'IT', 'IT', 'HR', 'HR', 'Sales', 'IT', 'HR', 'Sales'],
    'salary': [50000, 55000, 70000, 80000, 48000, 52000, 60000, 90000, 51000, 45000],
    'rating': [4.5, 4.9, 3.8, 4.2, 4.1, 3.9, 4.6, 4.7, 4.3, 3.5],
})

plt.figure(figsize=(8, 5))

sns.histplot(
    data=data,
    x='salary',
    bins=10,
    color='blue',
    kde=True,
)

plt.title('Salary Distribution')
plt.xlabel('Salary ($)')
plt.ylabel('Count')

plt.show()