import math
#Print all factors of a given number in list format
# num = 15
# n = num
# r = []
# for i in range (1,n+1):
#     if n%i==0:
#         r.append(i)
#     else:
#         pass
# print(r)
print('''T.C = O(n) and S.C = O(k) where k = is the no of factors stored in'r' ''')
'''             BUT BUT BUT, THE ABOVE SOLUTION IS VERY BRUTE (WE HAVE TO MAKE IT MORE OPTIMIZED)
'''
'''SINCE WE KNOW THAT FACTORS OF FOR EX 20 ARE = [1,2,4,5,10,20]
NOTICE HOW AFTER HALF OF THE NUMBER (20 IN THIS EX) WE DON'T
GET ANY FACTORS OTHER NO ITSELF? - THAT'S IT!! WE ARE GONNA USE THIS 
TO OPTIMIZE THE ABOVE SOLN EVEN MORE NOW:-'''
# k = num
# s = []
# for i in range (1,k//2):
#     if k%i==0:
#         s.append(i)
#     else:
#         pass
# s.append(k)
# print(s)
print('''T.C = O(n/2) and S.C = O(k) where k = is the no of factors stored in's' ''')
'''         BUT BUT BUT  THE T.C IS STILL ALMOST EQUAL TO O(N), HENCE MORE
OPTIMIZATION!!!!'''

n = 36
num = int(math.sqrt(n))
r = [1,n]
for i in range(2,num+1):
    if n%i==0:
        r.append(i)
    if n//i != i:
        r.append(n//i)
r.sort()#t.c = O(nlogn)
print(r)
#THEREFORE T.C = O(sqrt(n))+O(nlogn)
#S.C = O(k)