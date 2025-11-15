import numpy as np
a = np.array([1,2,3,4])
a*=2
b=np.array([[1,2,3],[3,4,5]])
print(a)
print(type(a))
print(a.ndim)
print(b)
print(b.ndim)
print(b.shape)
c =np.array([
            [[1,2,3],[4,5,6],[7,8,9]],
            [[10,11,12],[13,14,15],[16,17,18]],
            [[19,20,21],[22,23,24],[25,26,27]]
            ])
print(c.shape)
print(c[2][1][0])
print(c[0,0,1])
print(c.ndim)