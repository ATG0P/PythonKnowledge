import numpy as nm
l1 = nm.array('a')
print(l1.ndim)
l2 = nm.array([1,2,4,5,6])
print(l2.ndim)
l3 = nm.array([[1,2,3],[4,5,6]])
print(l3.ndim)
# l4 = nm.array([[['a','b','c'],['d','e','f'],['g','h','i']],
#               [['j','k','l'],['m','n','o'],['p','q','r']],
#               [['s','t','u'],['v','w','x'],['y','z']]])
'''if I run the code with the above array, it will give the output as :-
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 2 dimensions. The detected shape was (3, 3) + inhomogeneous part.

It's becuz in the last array, you are supposed to have 3 elements to maintain the homogenity. Improved code below '''

l4 = nm.array([[['a','b','c'],['d','e','f'],['g','h','i']],
              [['j','k','l'],['m','n','o'],['p','q','r']],
              [['s','t','u'],['v','w','x'],['y','z','']]])
print(l4.ndim)
print(l4.shape)#(no of element in outermost,no of element in middle,no of element in innermost)
l5= nm.array([
            [['a'],['d'],['g']],
            [['j'],['m'],['p']]
            ])
print(l5.shape)
print(l3.shape)