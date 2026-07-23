# Merge DataFrames with mismatched key columns using left_on and right_on
import pandas as pd
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'dept_id': [101, 102, 101, 103, 102]
})

departments = pd.DataFrame({
    'dept_number': [101, 102, 103],
    'dept_name': ['Sales', 'IT', 'HR'],
    'location': ['Mumbai', 'Delhi', 'Chennai']
})
merged_ids = pd.merge(employees, departments, left_on='dept_id', right_on='dept_number')
merged_ids = merged_ids.drop(columns=['dept_number'])

print(merged_ids[['name', 'dept_name', 'location']])