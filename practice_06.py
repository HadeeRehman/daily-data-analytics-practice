# Question: Separate a list of numbers into Even and Odd groups inside a dictionary.

report = {
    'Even': [],
    'Odd': []
}
numbers = [1, 2, 3, 4, 5, 6]
 
for num in numbers:
    if num % 2 == 0:
        report['Even'].append(num)
    else:
        report['Odd'].append(num)
print(report['Even'])
print(report['Odd'])
