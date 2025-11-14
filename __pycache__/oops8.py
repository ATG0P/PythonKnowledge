from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side*self.side
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5*self.base*self.height
class Pizza(Circle):
    def __init__(self,topping, radius):
        super().__init__(radius)
        self.topping = topping
shapes = [Circle(10),Square(5),Triangle(4,5),Pizza("pepperoni",5)]
for a in shapes:
    print(a.area())
