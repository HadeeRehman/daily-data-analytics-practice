# Question: Convert student marks into grades 'A' or 'B' using two different methods.
students = [
    {"name": "Hadi", "marks": 92},
    {"name": "Ali", "marks": 75},
    {"name": "Omar", "marks": 88},
    {"name": "Sara", "marks": 95}
]

report = {}

for student in students:
    if student['marks'] >= 80:
        student['marks'] = 'A'
    else:
        student['marks'] = 'B'
    report[student['name']] = student['marks']
print(report)

# Method 2: Mapping directly to a new dictionary
students = [
    {"name": "Hadi", "marks": 92},
    {"name": "Ali", "marks": 75},
    {"name": "Omar", "marks": 88},
    {"name": "Sara", "marks": 95}
]
report2 = {}

for student in students:
    if student['marks'] >= 80:
        report2[student['name']] = 'A'
    else:
        report2[student['name']] = 'B'
print(report2)

# Another Way Is Creating New Dict As Grade
students = [
    {"name": "Hadi", "marks": 92},
    {"name": "Ali", "marks": 75},
    {"name": "Omar", "marks": 88},
    {"name": "Sara", "marks": 95}
]

report3 = {}

for student in students:
    if student['marks'] >= 80:
        student['Grade'] = 'A'
    else:
        student['Grade'] = 'B'
    report3[student['name']] = student['Grade']
print(report3)