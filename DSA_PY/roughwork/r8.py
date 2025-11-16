import numpy as np

a1=np.array([1,2,4,5,6,4,3234,324324,32])
a2=a1[a1%2==0]
print(a2)