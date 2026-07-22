# Handle missing data in Pandas using fillna()

import pandas as pd
import io
csv_data = """name,dept,salary,rating
Alice,Sales,50000,4.5
Bob,IT,,3.8
Charlie,Sales,55000,
Diana,IT,80000,4.2
Eve,,45000,3.5
Frank,IT,90000,4.7
Grace,HR,,4.1
Hank,HR,52000,"""
df = pd.read_csv(io.StringIO(csv_data))

print(df.isnull().sum()) 

df = df.fillna(
    {"salary": df["salary"].mean().round(2), "rating": 0.0, "dept": "Unknown"}
)

print("\n       === CLEANED DATAFRAME ===\n")
print(df)