import numpy as np
#level 1
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])
print(arr[:2,1:3])
print(arr[2:,2:])
print(arr[1])
print(arr[-1:,:])#sorry this is a little tricky one
#level 2
arr = np.arange(1, 26).reshape(5, 5)

print(arr[1:3,1:4])
print(arr[::4,::4])
print(arr[:,::4])#both diagonal and anti-diagonal are hard as well



#level 3
arr = np.arange(1, 101).reshape(10, 10)
print(arr[::2])#printing alternate rows
print(arr[:,::2])#printing alternate columns
print(arr[3:7,3:7])
print(arr[arr%2==0])
print(arr[::4,3:9])#I might have misunderstood this question tho
arr[:,:5]=0
print(arr)