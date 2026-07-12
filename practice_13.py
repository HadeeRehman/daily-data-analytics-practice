# Question: Calculate total sales per city and rank the cities from highest to lowest revenue.
sales = [
    {"city": "Mumbai",  "product": "Laptop", "amount": 1200},
    {"city": "Delhi",   "product": "Phone",  "amount": 800},
    {"city": "Mumbai",  "product": "Tablet", "amount": 400},
    {"city": "Chennai", "product": "Laptop", "amount": 900},
    {"city": "Delhi",   "product": "Laptop", "amount": 1100},
    {"city": "Chennai", "product": "Phone",  "amount": 600},
    {"city": "Mumbai",  "product": "Phone",  "amount": 700},
    {"city": "Delhi",   "product": "Tablet", "amount": 300},
]
def top_cities(sales):
    data = {}
    for sale in sales:
        if sale['city'] not in data:
            data[sale['city']] = {'total': 0}
        data[sale['city']]['total'] += sale['amount']
    # result = {}
    # for city in data:
    #     result[city] = data[city]['total']
    # new = result.items()
    # return sorted(new, key= lambda x: x[1], reverse=True) # lambda x : x[1] # "what to compare while sorting."
    return sorted([(city, data[city]['total']) for city in data], key=lambda x: x[1], reverse=True) # same answer with list comprehension 
print(top_cities(sales))