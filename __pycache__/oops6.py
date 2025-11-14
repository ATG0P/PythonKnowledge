from abc import ABC,abstractmethod
 
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("Your car can go")
    def stop(self):
        print("Your car can stop")
car = Car()
car.go()
car.stop()