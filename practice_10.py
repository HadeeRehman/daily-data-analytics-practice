# Question: Calculate the average salary for each department.

# --- Step 1: Accumulate total salaries and counts per department ---

# --- Step 2: Loop through the aggregated data to calculate the rounded averages ---

employees = [
    {"name": "Alice",   "dept": "Sales",  "salary": 50000},
    {"name": "Bob",     "dept": "IT",     "salary": 70000},
    {"name": "Charlie", "dept": "Sales",  "salary": 55000},
    {"name": "Diana",   "dept": "IT",     "salary": 80000},
    {"name": "Eve",     "dept": "Sales",  "salary": 45000},
    {"name": "Frank",   "dept": "IT",     "salary": 90000},
    {"name": "Grace",   "dept": "HR",     "salary": 48000},
    {"name": "Hank",    "dept": "HR",     "salary": 52000},
]
def avg_salary_by_dept(employees):
    data = {}
    for sale in employees:
        if sale['dept'] not in data: 
            data[sale['dept']] = {'count': 0, 'total': 0}
        data[sale['dept']]['count'] += 1 # 0 + sales = 1
        data[sale['dept']]['total'] += sale['salary'] # 0 + sale[salary] = 50000
    average = {}
    for dept in data: # because here data is dict now and dept is key inside it
        total = data[dept]['total']  
        count = data[dept] ['count'] 
        average[dept] = round(total / count, 2)
    return average
print(avg_salary_by_dept(employees))