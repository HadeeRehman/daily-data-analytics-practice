# Question: Group students into Passed or Failed lists based on their marks.
# Students with 80 or more marks pass.

students = [
    {"name": "Hadi", "marks": 92},
    {"name": "Ali", "marks": 75},
    {"name": "Omar", "marks": 88},
    {"name": "Sara", "marks": 95}
]

report = {
    "Passed": [],
    'Failed' : []
}

for student in students:
    if student['marks'] >= 80:
        report["Passed"].append([student['name'],student['marks']])
    else:
        report['Failed'].append([student['name'],student["marks"]])
print(report)