class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower


class Wheel:
    def __init__(self,size):
        self.size = size

class Car:
    def __init__(self,make,model,horsepower,size):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)#aggreagation where one object is dependent on another object
        self.wheels = Wheel(size)
    def display_car_details(self):
        return f"{self.make}, {self.model} , {self.engine.horsepower}, {self.wheels.size}"

car1 = Car("Maruti Suzuki","Balleno",500,20)
car2 = Car("Lamborgini","Urus",600,18)
print(car1.display_car_details())
print(car2.display_car_details())