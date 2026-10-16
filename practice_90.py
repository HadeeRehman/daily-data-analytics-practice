# Split delimited string columns into multiple DataFrame columns using str.split with expand=True
import pandas as pd

data = {
    'full_name': ['Johnathan Doe', 'Jane Smith', 'Robert Johnson', 'Emily Davis'],
    'location': ['New York, NY', 'Austin, TX', 'Seattle, WA', 'Chicago, IL'],
}

df = pd.DataFrame(data)

# 1. Split full name on the first whitespace occurrence
df[['first_name', 'last_name']] = df['full_name'].str.split(' ', n=1, expand=True)

# 2. Split location into city and state using a comma delimiter
df[['city', 'state']] = df['location'].str.split(', ', expand=True)

print(df)