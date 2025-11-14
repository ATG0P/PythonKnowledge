s = input("ENTER ROMAN NUMERALS: ")
r = 0 
for i in s:
    if i == 'IV':
        r+=4
    elif i == "IX":
        r+=9
    elif i=='XL':
        r+=40
    elif i == "XC":
        r+=90
    elif i == "CD":
        r+=400
    elif i=='CM':
        r+=900
    elif i=="I":
        r+=1
    elif i=="V":
        r+=5
    elif i=='X':
        r+=10
    elif i=='L':
        r+=50
    elif i=='C':
        r+=100
    elif i=='D':
        r+=500
    elif i=='M':
        r+=1000
print(r)