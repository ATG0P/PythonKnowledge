x=121
k=x
y=x
count=-1
z=0
while True:
    if(y==0):
        break
    else:
        y=y//10
        count+=1
while True:
    if(x==0):
        break
    else:
        z+=(x%10)*(10**count)
        count-=1
        x=x//10
if(k==z):
    print(True)
else:
    print(False)