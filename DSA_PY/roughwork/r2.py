s = " "
b =  []
k = 0
r=0
for i in range(0,len(s)):
    if s[i] in b:
        if r>k:
            pass
        else:
            r=k
        k=1
    else:
        k+=1
        b.append(s[i])
print(r)