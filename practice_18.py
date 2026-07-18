# Raw Sales Transaction Data
sales = [
    {"day": "Monday",    "item": "Laptop",  "amount": 800},
    {"day": "Tuesday",   "item": "Phone",   "amount": 400},
    {"day": "Wednesday", "item": "Laptop",  "amount": 800},
    {"day": "Thursday",  "item": "Tablet",  "amount": 300},
    {"day": "Friday",    "item": "Phone",   "amount": 400},
    {"day": "Saturday",  "item": "Laptop",  "amount": 800},
    {"day": "Sunday",    "item": "Tablet",  "amount": 300},
]
def total_by_item(sales):
    totals = {}
    for sale in sales:
        item = sale['item']
        amount = sale['amount']
        if item in totals:
            totals[item] += amount
        else:
            totals[item] = amount
    return totals
print(total_by_item(sales))


# Calculates totals using the optimized, pythonic dictionary .get() method.
def total_by_sales(sales):
    count = {}
    for sale in sales:
        count[sale['item']] = count.get(sale['item'], 0 ) + sale['amount']
    return count
print(total_by_sales(sales))