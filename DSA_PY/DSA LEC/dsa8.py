#check if a number is an armstrong number or not
num = 153
n = num 
a = []
b=0
count=0
while n>0:
    a.append(n%10)
    n = n//10
    count+=1
for i in a:
    b+= i**count
if b==num:
    print("Yes")
else:
    print("No")
print("Time Complexity = O(log10 N)")
print("Space Complexity = O(1)")