class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"it is of {self.color} color and is {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self): #this method will overwrite different() from Shape class
        print(f"Area of circle is {3.14 * self.radius * self.radius}")
class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side
    def describe(self):
        super().describe()
        print(f"It is a area of {self.side * self.side}")
    
    
class Rectangle(Shape):
    def __init__(self, color, is_filled, length, breadth):
        super().__init__(color, is_filled)
        self.length = length
        self.breadth = breadth

r = Rectangle("Red",True,10,5)
print(r.is_filled)
r.describe()

circle = Circle("black",True,10)
circle.describe() #will overwrite and calculate area

s = Square("red",True,10)
s.describe()