# str="3-gatsu no Lion 2nd SeasonTV (22 eps)Oct 2017 - Mar 2018388,358 members"
# s=str.index('(')
# e=str.index(' eps)')
# num=""
# for i in range (s+1,e+1):
#     num+=str[i]
# num=int(num)
# print(num)

# str="3-gatsu no Lion 2nd SeasonTV (22 eps)Oct 2017 - Mar 2018388,358 members"
# s=str.find(")")
# e=s+19
# r=""
# for i in range(s+1,e+1):
#     r+=str[i]
# print(r)


str="3-gatsu no Lion 2nd SeasonTV (22 eps)Oct 2017 - Mar 2018388,358 members"
s=str.find(")")
e=s+19
y2=""
y1=""
for i in range(s+1,e+1):
    if (str[i].isdigit() and i<=s+8):
        y1+=str[i]
    elif(str[i].isdigit() and i>s+8):
        y2+=str[i]

y2=int(y2)
print(type(y2))