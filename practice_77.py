# Combine relational tables using inner and left joins in pd.merge
import pandas as pd

# Left table: Employee records
employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'dept_id': ['D1', 'D2', 'D1', 'D4'],
})

# Right table: Department lookup table
departments = pd.DataFrame({
    'dept_id': ['D1', 'D2', 'D3'],
    'dept_name': ['Human Resources', 'Engineering', 'Marketing'],
})

# Inner Join: Keeps only rows where dept_id exists in both tables
inner_join = pd.merge(employees, departments, on='dept_id', how='inner')

# Left Join: Keeps all employees, fills missing department names with NaN
left_join = pd.merge(employees, departments, on='dept_id', how='left')

print("--- Inner Join (Exact matches only) ---")
print(inner_join[['emp_id', 'name', 'dept_name']])

print("\n--- Left Join (Preserves all left-table records) ---")
print(left_join[['emp_id', 'name', 'dept_name']])