# Create a bar chart and add value labels to each bar using plt.text()
import matplotlib.pyplot as plt

departments = ['Sales', 'IT', 'HR', 'Marketing', 'Finance']
headcount = [25, 18, 8, 12, 15]

plt.bar(departments, headcount, color='skyblue')

# i → x position, value → y position, value  → text to display OR plt.text(x, y, label)
for i, value in enumerate(headcount):
    plt.text(i, value, value)

plt.title('Headcount by Department', fontsize=10,
          fontweight='bold',
          )
plt.show()