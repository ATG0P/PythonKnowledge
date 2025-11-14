class Student:

    class_year = 2024
    num_student = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_student +=1 

student1 = Student("Aryan",17)
print(Student.num_student)  #output = 1
student2 = Student("Anjali",14)
print(Student.num_student)  #output = 2 (since 2 objects have been created and therefore __init__ func have been called 2 times)
print(f"my graduating class of year {Student.class_year} has {Student.num_student} students which are : ")
print([f"{student1.name}",f"{student2.name}"])