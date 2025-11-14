class Studentss:
    num_students = 0
    def __init__(self,name,rollno,gender):
        self.name = name
        self.rollno = rollno
        self.gender = gender
        Studentss.num_students+=1

a = int(input("Enter the no of students you for entry: "))
b = []
for i in range(1,a+1):
    n = input("Name: ")
    r = int(input("Age: "))
    g = input("Gender: ")
    s = Studentss(n,r,g)
    b.append(n)
    b.append(r)
    b.append(g)
print("No of students enrolled:",Studentss.num_students)
i = 0
while(i<=len(b)-3):
    print("Name:",b[i]," Age:",b[i+1]," Gender:",b[i+2])
    i+=3