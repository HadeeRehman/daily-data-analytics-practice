# Parse timestamps and extract calendar features using pd.to_datetime and dt accessor
import pandas as pd

data = {
    'event_id': [101, 102, 103, 104, 105],
    'timestamp_str': [
        '2026-03-14 09:30:00',
        '2026-03-15 14:15:00',
        '2026-03-16 18:45:00',
        '2026-03-20 22:10:00',
        '2026-03-22 11:00:00',
    ],
}

df = pd.DataFrame(data)

# 1. Parse string timestamps into native datetime64[ns] dtype
df['timestamp'] = pd.to_datetime(df['timestamp_str'])

# 2. Extract calendar and time components using the .dt accessor
df['month_name'] = df['timestamp'].dt.month_name()
df['day_name'] = df['timestamp'].dt.day_name()
df['hour'] = df['timestamp'].dt.hour

# 3. Engineer a boolean weekend indicator (Saturday=5, Sunday=6)
df['is_weekend'] = df['timestamp'].dt.dayofweek.isin([5, 6])

print(df[['event_id', 'timestamp', 'day_name', 'hour', 'is_weekend']])