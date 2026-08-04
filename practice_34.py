# Calculate basic summary statistics and filter values in NumPy
import numpy as np

scores = np.array([85, 92, 78, 90, 55, 88, 72, 95, 60, 83])

print(np.mean(scores))
print(np.median(scores))
print(np.std(scores))
print(np.min(scores))
print(np.max(scores))
print(scores[scores >= 80])
print(np.argmax(scores))