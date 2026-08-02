# Group data by multiple columns and aggregate mean salary by seniority
import pandas as pd
import io

csv_data = """name,dept,salary,rating
Alice,Sales,50000,4.5
Bob,IT,70000,3.8
Charlie,Sales,55000,4.9
Diana,IT,80000,4.2
Eve,Sales,45000,3.5
Frank,IT,90000,4.7
Grace,HR,48000,4.1
Hank,HR,52000,3.9"""

df = pd.read_csv(io.StringIO(csv_data))

grouped_dept = df.groupby('dept')['salary'].mean().reset_index()
def classify(value):
    if value >= 70000:
        return 'Senior'
    else:
        return 'Junior'
df['Seniority'] = df['salary'].apply(classify)

grouped_both = df.groupby(['dept', 'Seniority'])['salary'].mean().reset_index()

print(grouped_both.to_string(index=False))