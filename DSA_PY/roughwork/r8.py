import numpy as np
#level 1
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])
print(arr[0:2,1:3])
print(arr[2:,2:])
print(arr[:,1])
print(arr[::-1])
print(arr[:,::-1])

#Level 2 
arr=np.arange(1,26).reshape(5,5)
'''
[
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
16,17,18,19,20
21,22,23,24,25
]
'''
print(arr[1:3,1:4])
print(arr[::4,::4])
#print(arr[::1,::1])#this one is areally tough
#print(arr[])#so is the ant-diagonal one

#Level 3
arr=np.arange(1,101).reshape(10,10)
print(arr[::2,::2])
print(arr[3:7,3:7])
print(arr[arr%2==0])
print(arr[2:8,::3])
arr[:,:5]=0
print(arr)
