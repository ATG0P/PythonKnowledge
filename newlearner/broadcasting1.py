import numpy as np
'''
Broadcasting allows NumPy to perform operations on array
with different shapes by virtually expanding dimensions
so they match the larger array's shape
RULES:-
The dimensions have the same size
OR
One of the dimensions has a size of 1 but not both should be necessarily be 1'''

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])
print(array1.shape)#(1,4) 
print(array2.shape)#(4,1)
'''since in both shape either row is 1 or column is 1
therefore:-'''
print(array1*array2,"\n")
array3 = np.array([[1,2,3,4],
                   [5,6,7,8]])
# print(array2*array3)#(4,1)*(2,4) therefore ValueError
print(array3*array1)#(2,4)*(1,4) herefore it worked since 4 and 4 match
