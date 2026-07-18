# Question : Use length of name as value 
students = [
    {"name": "Hadi", "marks": 92},
    {"name": "Ali", "marks": 75},
    {"name": "Omar", "marks": 88},
    {"name": "Sara", "marks": 95}
]

report = {}

for student in students:
    report[student['name']] = len(student['name'])
print(report)

# Question : Take names from given list and keep there length as value in new dict
names = ["hadi", "ali", "omar", "sarah"]

report = {}
for name in names:
    report[name] = len(name)
print(report)
