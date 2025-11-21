import numpy as np
rng = np.random.default_rng(seed=1)#this will assign the random number a code (here 1) and willbe kept recorded foever
print(rng.integers(1,11))
print(np.random.uniform(low=-1,high=1))#here uniform means equal chances of all number to be printed