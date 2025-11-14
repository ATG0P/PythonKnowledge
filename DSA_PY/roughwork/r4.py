a = int(input("Enter a number: "))
print("Even numbers from 1 to ",a," are :- ")
for i in range(1,a+1):
    if(i%2==0):
        print(i)
    else:
        continue