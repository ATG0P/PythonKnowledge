import numpy as np
arr = np.array([
                [1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]
                ])
#array[start:end:step] NOTE: end index is exclusive
# print(arr[0:4])
# print(arr[0:4:2]) #output: [[1,2,3,4] [9,10,11,12]]
# print(arr[::2])#same as above
# print(arr[::-1])#will  print the lists from below
# print(arr[::-2])

'''NOW WE ARE GONNA DO A COLUMN SELECTION:- '''
# print(arr[:,0])#[first row:last row, column] - it is gonna print all the first element in a list(basically 1st column)
# print(arr[:,1])#print all the second element in a list(basically 2nd column)
# print(arr[:,-1])#print last column
# print(arr[:,0:3])#print first 3 column of each row
# print(arr[0:3,::2])
print(arr[0:2,2:4])