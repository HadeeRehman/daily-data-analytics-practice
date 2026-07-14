# Question: Parse a raw CSV string into a list of dictionaries with proper data type conversion.
csv_data = """name,subject,score
Alice,Math,88
Bob,Science,55
Charlie,Math,72
Diana,Science,91
Eve,Math,40
Frank,Science,78
Grace,Math,95
Hank,Science,43"""

def parse_csv(csv_data):
    data = []
    lines = csv_data.splitlines()
    header = lines[0].split(",")
    for line in lines[1:]:
        student = {}
        values = line.split(",")
        for key, value in zip(header, values): # Takes 1 item at a time like: header = name then value = alice not whole thing at one time
            if key == 'score':
                student[key] = int(value)
            else:
                student[key] = value
        data.append(student)
    return data

print(parse_csv(csv_data))