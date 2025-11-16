import numpy as np
#Filtering refers to the process of selecting elements from an array that match a given 
#condition 
age = np.array([
                    [17,13,19,20,45,19,56,78,92,43],
                    [82,36,31,27,14,67,14,33,22,46]
                    ])
Cannot_Drive = age[age<18]
Can_Drive=age[(age>=18) & (age<=65)]#numpy uses C logical operators and maybe that's why its fast
Retired_Drivers = age[age>65]
print(Can_Drive)
print(Cannot_Drive)
print(Retired_Drivers)

adults = np.where(age>=18,age,18) #it will create an array from array 'age' and replace the the element with 18 if the given conditon does not get satisfied
print(adults)