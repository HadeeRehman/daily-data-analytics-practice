# Plot styled correlation matrix heatmap with fixed bounds and cell borders
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

np.random.seed(42)
data = pd.DataFrame({
    'salary': np.random.normal(60000, 15000, 100),
    'rating': np.random.normal(4.0, 0.5, 100),
    'experience': np.random.normal(5, 2, 100),
    'age': np.random.normal(35, 8, 100),
})

corr = data.corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr,
    cmap='coolwarm',
    annot=True,
    fmt='.2f',  # Clean decimal formatting
    vmin=-1,
    vmax=1,  # Anchor scale to full correlation range [-1, 1]
    linewidths=0.5,  # Add clean borders between cells
    square=True,  # Force square cell aspect ratio
)

plt.title('Feature Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()