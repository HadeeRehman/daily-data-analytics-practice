# Categorize salary levels and calculate bonuses using apply() and lambda functions
import pandas as pd
import io

csv_data = """name,salary,rating,dept
Alice,50000,4.5,Sales
Bob,70000,3.8,IT
Charlie,55000,4.9,Sales
Diana,80000,4.2,IT
Eve,45000,3.5,Sales
Frank,90000,4.7,IT
Grace,48000,4.1,HR
Hank,52000,3.9,HR"""

df = pd.read_csv(io.StringIO(csv_data))

def classify(value):
    if value < 50000:
        return 'Junior'
    elif value < 70000:
        return 'Mid'
    else:
        return 'Senior'
df['salary_level'] = df['salary'].apply(classify)
def status(value):
    if value < 3.8:
        return 'Low'
    elif value < 4.5:
        return 'Good'
    else:
        return 'Excellent'
df['performance'] = df['rating'].apply(status)
df['bonus'] = df.apply(lambda row: round(row['salary'] * (row['rating'] / 10 ), 2), axis=1)