# Calculate weighted performance scores and rank employees using np.dot and argsort
import numpy as np

# 4 employees, 3 KPIs (sales, quality, attendance)
performance = np.array([
    [0.8, 0.9, 0.95],
    [0.6, 0.7, 0.80],
    [0.9, 0.8, 0.90],
    [0.7, 0.6, 0.75]
])

# weights for each KPI
weights = np.array([0.5, 0.3, 0.2])

# "np.dot() multiplies matching elements of two arrays and adds the products to produce a single value (or one value per row when using a matrix)."

weighted_scores = np.dot(performance, weights) 

top_performer = np.argmax(weighted_scores) + 1

normalized_score = (weighted_scores - np.min(weighted_scores)) / (np.max(weighted_scores) - np.min(weighted_scores))

ranked_employees = np.argsort(weighted_scores)[::-1] # sortes using index and also label index

print(ranked_employees)