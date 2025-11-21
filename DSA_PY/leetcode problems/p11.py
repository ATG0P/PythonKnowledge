height = [1,8,6,2,5,4,8,3,7]
tallest = 0
r=0
index1=0
index2=0
for i in range(0,len(height)):
    if(height[i]>tallest):
        tallest=height[i]
        index1=i
    else:
        continue    
k=tallest
height.remove(tallest)
tallest=0
l=len(height)
while(l>0):
    if(height[i]==k):
        height.pop(i)
        index2+=1
    elif(height[i]>=tallest):
        tallest=height[i]
        r=tallest
        index2=i
    else:
        continue
    l=len(height)
    l-=1
print(index2)
print(index1)
print(index2-index1)