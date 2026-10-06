# Compute rolling moving averages and percent growth using rolling and pct_change
import pandas as pd

# Daily revenue tracking across 10 consecutive business days
data = {
    'date': pd.date_range(start='2026-01-05', periods=10, freq='D'),
    'revenue': [1200, 1450, 1300, 1650, 2100, 1950, 2300, 2400, 2150, 2700],
}

df = pd.DataFrame(data)

# 1. Calculate a 3-day simple rolling moving average
df['rolling_3d_avg'] = df['revenue'].rolling(window=3).mean()

# 2. Calculate day-over-day percentage growth
df['pct_growth'] = df['revenue'].pct_change() * 100

# Format percentage for cleaner console reading
df['pct_growth'] = df['pct_growth'].round(2)
df['rolling_3d_avg'] = df['rolling_3d_avg'].round(2)

print(df)