import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
product_a = [100, 120, 115, 140, 160, 155]
product_b = [80, 85, 95, 100, 110, 130]
product_c = [60, 70, 65, 90, 95, 105]

plt.figure(figsize=(10, 6))
 
plt.plot(months, product_a, color='green', label='Product A')
plt.plot(months, product_b, color='blue', label='Product B')
plt.plot(months, product_c, color='purple', label='Product C')

plt.title('Product Sales Comparison')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.show()