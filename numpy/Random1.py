import numpy as np
rng = np.random.default_rng()
print(rng.integers(1,100))
print(rng.integers(low = 1, high =101, size=3))#high is exclusive
print(rng.integers(low = 1, high =101, size=(3,2)))#3 rows and 2 columnsb
print(rng.random())