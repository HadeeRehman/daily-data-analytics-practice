# Question: Parse raw employee CSV data and group high performers (rating >= 4.0) alphabetically by department.
csv_data = """name,dept,salary,rating
Alice,Sales,50000,4.5
Bob,IT,70000,3.8
Charlie,Sales,55000,4.9
Diana,IT,80000,4.2
Eve,Sales,45000,3.5
Frank,IT,90000,4.7
Grace,HR,48000,4.1
Hank,HR,52000,3.9"""

def parse_csv(csv_data):
    data = []
    lines = csv_data.splitlines()
    header = lines[0].split(",")
    for line in lines[1:]:
        values = line.split(",")
        student = {}
        for key, value in zip(header, values):
            if key == 'salary':
                student[key] = int(value)
            elif key == 'rating':
                student[key] = float(value)
            else:
                student[key] = value
        data.append(student)
    return data
print(parse_csv(csv_data))


employees = parse_csv(csv_data)
def high_performers(employees):
    data = {}
    for employee in employees:
        if employee['dept'] not in data:
            data[employee['dept']] = []
        if employee['rating'] >= 4.0:
            data[employee['dept']].append(employee['name'])
    # return {dept: sorted(data[dept]) for dept in data}
    for dept in data:
        data[dept] = sorted(data[dept]) # data["Sales"] = ["Alice", "Charlie"] Note: sorted goes inside REMEMBER THIS
    return data
print(high_performers(employees))
