# Plot scatter plot with colormap and linear regression trend line
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
hours_studied = np.random.uniform(1, 10, 50)
exam_scores = hours_studied * 8 + np.random.normal(0, 10, 50) # exam_score = 72 + 6.5 = 78.5


plt.scatter(hours_studied, exam_scores, c=exam_scores, cmap='viridis')
plt.colorbar(label='Score')

plt.title('Distribution of Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')

# y = mx + b,  m = slope → how steep the line is, b = intercept → where the line starts on the y-axis, The 1 tells you I want a straight line."
"Find the best straight line describing the relationship between hours studied and exam scores."
m, b = np.polyfit(hours_studied, exam_scores, 1)
trend = m * hours_studied + b # y = mx + b
plt.plot(hours_studied, trend, color='red')


plt.show()