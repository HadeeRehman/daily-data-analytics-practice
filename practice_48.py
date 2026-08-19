# Create a 2x2 subplot dashboard with line, bar, and pie charts

import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue = [12000, 15000, 13500, 18000, 22000, 19500]
expenses = [8000, 9500, 9000, 11000, 13000, 12500]
departments = ['Sales', 'IT', 'HR', 'Marketing']
headcount = [25, 18, 8, 12]

figure, axes = plt.subplots(2, 2)
axes[0, 0].plot(months, revenue, color='blue')
axes[0, 0].set_title('Graph of Revenue')

axes[0, 1].plot(expenses, color='red')
axes[0, 1].set_title('Graph of Expenses')

axes[1, 0].bar(departments, headcount, color='skyblue')
axes[1, 0].set_title('Distribution of Departments')

axes[1, 1].pie(headcount, labels=departments,
               autopct='%1.1f%%',
               )

plt.tight_layout()
plt.show()