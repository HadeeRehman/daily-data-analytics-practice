# Generate random integers, floats, and normal distributions using NumPy
import numpy as np

#np.random.seed(42) is a setting, not a value.
np.random.seed(42)

rng = np.random.randint(low=1, high=101, size=10) # here we give range

rng_flaot = np.random.random(size=5) # here range is fixed i.e 0 to 1

# loc is the center (average) around which the random numbers are generated. like 45, 48, 50, 52, 55
# scale controls how spread out the numbers are from the center (loc).
data = np.random.normal(loc=50, scale=10, size=1000)
print(np.mean(data), np.std(data))
