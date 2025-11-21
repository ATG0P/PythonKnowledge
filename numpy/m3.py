import numpy as nm
a = nm.array([
            [[1,2,3],[4,5,6],[7,8,9]],
            [[10,11,12],[13,14,15],[16,17,18]],
            [[19,20,21],[22,23,24],[25,26,27]]
            ])
print(a.shape)
print(a[0][0][1]) #chain indexing
print(a[0,0,1])#Multi indexing- faster than chain indexing

l4 = nm.array([[['a','b','c'],['d','e','f'],['g','h','i']],
              [['j','k','l'],['m','n','o'],['p','q','r']],
              [['s','t','u'],['v','w','x'],['y','z','']]])
let = l4[0,0,0]+l4[2,0,0]+l4[2,0,0]
print(let)