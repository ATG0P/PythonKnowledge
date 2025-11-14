class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    def employee_info(self):
        return f"{self.name} : {self.position}"
    
    @staticmethod
    def is_valid_postion(position):
        p = ["Manager","Cook","Waiter","Sweeper"]
        return position in p
    
employee = Employee("Aryan","Manager")
print(employee.employee_info())
print(Employee.is_valid_postion("Manager"))