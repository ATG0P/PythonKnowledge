n = int(input("Enter a number : "))
for i in range (1,n+1):
    for j in range (1,n+1):
        print()
#time complexity = O(n^2)

for i in range(1,n+1):
    for j in range(1,i+1):
        print()
''' 

            i   j
            1   1
            2   1,2
            3   1,2,3 
            4   1,2,3,4
            5   1,2,3,4,5
            |   |
            |   |
            |   |
            n   1,2,3,4,5,---,n
        therefore : tc = 1+2+3+4+5+---+n = n(n+1)/2 = (n^2)/2 +n/2
        therefore Time Complexity~=n^2
        '''