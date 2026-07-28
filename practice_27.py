# Clean string columns and practice row operations with apply()
import pandas as pd
import io

csv_data = """name,dept,email,salary
  alice ,sales,ALICE@gmail.com,50000
BOB,  IT  ,bob@GMAIL.COM,70000
Charlie,Sales,charlie@gmail.com,55000
diana,hr,DIANA@gmail.com,80000
  EVE,Sales,eve@gmail.com,45000"""

df = pd.read_csv(io.StringIO(csv_data))

df['name'] = df['name'].str.strip()
df['dept'] = df['dept'].str.strip()

df['name'] = df['name'].str.title() # makes only letter first as capital

df['dept'] = df['dept'].str.lower()

df['email'] = df['email'].str.lower()

filtered = df[df['email'].str.contains('gmail')] # A boolean array acts like a filter.True → Keep the row.False → Remove the row.

df['email'] = df['email'].str.replace('gmail.com', 'company.com')


print(df.to_string(index=False))


def bonus(row):
    return row['salary'] * row['rating'] / 10
df.apply(bonus, axis=1)