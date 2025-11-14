a = 5873
num = a
lg = []
while num>0:
    last_digit = num%10
    lg.append(last_digit)
    num = num//10 #opposite of % due to which instead of remainder it gives you quotient
print(lg)