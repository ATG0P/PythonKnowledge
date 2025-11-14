class Student:
    count = 0
    total_gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count+=1
        Student.total_gpa+=gpa
    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name}'s gpa = {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total no of student {cls.count}"  #cls means class so either you can use this or use Student.count
    @classmethod
    def get_total_gpa(cls):
        return f"Total gpa = {cls.total_gpa}"
    @classmethod
    def average_gpa(cls):
        avg = cls.total_gpa/cls.count
        return f"Average class gpa = {avg}"
student1 = Student("Aryan", 5)
student2 = Student("Aayush",2.0)
print(student1.get_info())
print(student2.get_info())
print(Student.get_count())#OR student1.get_count()
print(Student.get_total_gpa())
print(Student.average_gpa())