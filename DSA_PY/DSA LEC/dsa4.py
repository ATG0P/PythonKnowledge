'''         space complexity: memory space (represented by Big - oh notation)     
they are of two types:
1.auxiliary space: the extra space used to solve the program
2.input space: the space used to store the input'''

x = int(input("Enter a number : "))
y = int(input("Enter a number : "))
z = int(input("Enter a number : "))
#here, x,y,z are input spaces
total = x+y+z #total is an auxiliary space
print(total)
'''NOTE : don't do change the input unless asked for example: 
x = x+y+z
print(x)'''