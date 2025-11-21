import numpy as np 
array = np.array([  [1,2,3,4,5],
                    [6,7,8,9,10]])
print(np.sum(array))
print(np.mean(array))
print(np.std(array))#standard deviation
print(np.var(array))#variance
print(np.min(array,axis=0))
print(np.max(array))
print(np.argmin(array))#index of minimum number
print(np.argmax(array))#index of maximum number

print(np.sum(array, axis=0))#returns an array of sum of all colums (axis=1 is for rows btw)
print(np.sum(array, axis=np.argmin(array)))#basically, index=0