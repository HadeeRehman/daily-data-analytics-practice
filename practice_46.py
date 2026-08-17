# Plot score distribution histogram with reference lines using Matplotlib
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
test_scores = np.random.normal(70, 12, 200)  # 200 students, mean=70, std=12

plt.hist(test_scores, bins=20, color='green', ec='black') 

# axvline full form : ax -> axis, v -> vertical, line 
# plt.axvline() can draw a vertical line anywhere, not just in the center.

plt.axvline(test_scores.mean(), color='red', linestyle='--', label='Mean')
plt.axhline(20, color='green', label='test', linestyle='dashed') 

plt.legend()
plt.title('Distribution of Test Scores')
plt.xlabel('Test Score')
plt.ylabel('Number of Students')
plt.show()