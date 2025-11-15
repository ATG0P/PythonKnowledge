import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([2,4,9])
print(arr1+arr2)
print(arr2-arr1)
print(arr2/arr1)
print(arr2*arr1)
print(arr2%arr1)
print(arr2**arr1)

print(arr1>=arr2)
print(arr1==arr2)
print(arr1<=3)
print(arr2>=3)
arr1[arr1<=3]=0
arr2[arr2>=3]=0
print(arr1,arr2)
print("Hi")
