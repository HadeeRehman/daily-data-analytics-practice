# Question : Get only names from dict
students = [
    {"name": "Hadi", "marks": 92},
    {"name": "Ali", "marks": 75},
    {"name": "Omar", "marks": 88},
    {"name": "Sara", "marks": 95}
]

report = []

for student in students:
    report.append(student['name'])
print(report)
