#count the number of digits
#method - 1
count=0
num = 5873
n = num
while n>0:
    n = n//10
    count+=1
print(count)
'''time complexity for problems like these are:-
while ...:
    x =x//y   --->T.C = O(logy n)
THEREFORE T.C FOR THIS QUESTION = O(log10 n)
space complexity = O(1) because only 2 variables are used and therefore space is constant'''
#method - 2
from math import *
print(int(log10(num)+1))