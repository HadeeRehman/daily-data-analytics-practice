# Question: Find the highest-earning employee in each department.

# Step 1: Track the maximum salary and earner name dynamically per department 

# Step 2: Use a dictionary comprehension to extract only the department and top earner's name 

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
def top_earner_by_dept(employees):
    data = {}
    for employee in employees:
        if employee['dept'] not in data:
            data[employee['dept']] = {'name': None, 'highest': 0}
        if employee['salary'] > data[employee['dept']]['highest']:
            data[employee['dept']]['name'] = employee['name']
            data[employee['dept']]['highest'] = employee['salary']
    # result = {}
    # for dept in data:
    #     result[dept] = data[dept]['name'] 
    # return result
    return {dept: data[dept]['name'] for dept in data} # same answer with  list comprehension and just in one line
print(top_earner_by_dept(employees))