import numpy as np 
arr = np.array([2,3,4,6,7,8,9,12,13,16,17,23,25,27,34,37,201])
uf = 52
lf = -20
for i in arr:
    if (i>uf or i<lf):
        np.delete(i)

print(arr)