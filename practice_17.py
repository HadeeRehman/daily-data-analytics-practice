# Question: Calculate the total amount spent by each customer by flattening and aggregating nested order items.
orders = [
    {"order_id": 1, "customer": "Alice", "items": [{"product": "Laptop", "qty": 1, "price": 800}, {"product": "Mouse", "qty": 2, "price": 25}]},
    {"order_id": 2, "customer": "Bob",   "items": [{"product": "Phone", "qty": 1, "price": 600}]},
    {"order_id": 3, "customer": "Alice", "items": [{"product": "Tablet", "qty": 1, "price": 300}, {"product": "Keyboard", "qty": 1, "price": 50}]},
    {"order_id": 4, "customer": "Charlie","items": []},
    {"order_id": 5, "customer": "Bob",   "items": [{"product": "Laptop", "qty": 2, "price": 800}]},
    {"order_id": 6, "customer": "Charlie","items": [{"product": "Mouse", "qty": 3, "price": 25}]},
]
def customer_totals(orders):
    data = {}
    for order in orders:
        if order['customer'] not in data:
            data[order['customer']] = 0
        for item in order['items']:
            amount = item['qty'] * item['price']
            data[order['customer']] += amount
    # result = {}
    # for name in data:
    #     result[name] = data[name]
    # return result
    return {name: data[name] for name in data}
print(customer_totals(orders))