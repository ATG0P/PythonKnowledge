a = int(input("Enter your age : "))
if a>=80:#1st/BEST CASE
    print("S Senior")
elif a<80 and a>=60:#2nd
    print("Senior")
elif a<60 and a>=24:#3rd
    print("Working")
elif a<24 and a>=18:#4th
    print("Still in college")
elif a<18 and a>=4:#5th
    print("In school")
else:#6th WORST CASE
    print("It's still a baby")
#THEREFORE, Time complexity = O(6)
'''     DIFFERENT TYPES OF TC

1)BIG- OH () -->  WORST CASE
2)THETA --> AVERAGE CASE 
3)OMEGA -->BEST CASE '''