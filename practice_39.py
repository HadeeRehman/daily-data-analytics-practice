# Count unique elements and frequency distribution using unique and bincount
import numpy as np

departments = np.array(['Sales', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'HR'])
scores = np.array([4, 2, 3, 4, 1, 2, 4, 3, 2, 1])

# np.unique() also sorts the unique values alphabetically.
unique_dept = np.unique(departments, sorted=False) 

unique_dept_appear = np.unique(departments)

unique_depts, counts = np. unique(departments, return_counts=True) # gives seprate Two values

scores_appear = np.bincount(scores) # starts counting from 0 

counts = np.bincount(scores) 
common = np.argmax(counts) 


print(unique_dept)
