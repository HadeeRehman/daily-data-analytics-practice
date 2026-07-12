# Question: Generate a summary for each customer tracking their total delivered order count and total amount spent.

orders = [
    {"order_id": 1, "customer": "Alice", "amount": 120, "status": "delivered"}, # First iteration
    {"order_id": 2, "customer": "Bob",   "amount": 80,  "status": "pending"},
    {"order_id": 3, "customer": "Alice", "amount": 200, "status": "delivered"},
    {"order_id": 4, "customer": "Charlie","amount": 150, "status": "cancelled"},
    {"order_id": 5, "customer": "Bob",   "amount": 90,  "status": "delivered"},
    {"order_id": 6, "customer": "Alice", "amount": 50,  "status": "pending"},
    {"order_id": 7, "customer": "Charlie","amount": 300, "status": "delivered"},
]
def  customer_summary(orders):
    data = {}
    for order in orders:
        if order['customer'] not in data:
            data[order['customer']] = {'delivered_count': 0, 'total_spent': 0}
        if order['status'] == 'delivered':
            data[order['customer']]['delivered_count'] += 1
            data[order['customer']]['total_spent'] += order['amount']
    return data
print(customer_summary(orders))