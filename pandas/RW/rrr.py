s = input("Enter a string: ")
uc=0
lc=0
bs=0
for i in s:
    if i.isupper():
        uc+=1
    elif i.islower():
        lc+=1
    elif i== " ":
        bs+=1
print(uc,lc,bs)