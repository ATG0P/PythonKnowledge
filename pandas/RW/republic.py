txt="Republic of India"
s=txt.find("R")
e=s+7
r=""
for i in range(s,e+1):
    r+=txt[i]
print(r)
if(r=="Republic"):
    print(True)
else:
    print(False)