class Animal:
    def __init__(self,name):
        self.name = name
        self.is_Alive = True
class Dog(Animal):
    def speak(self):
        print("Woof")
class Cat(Animal):
    def speak(self):
        print("Meow")
class Mouse(Animal):
    def speak(self):
        print("Squeek")
dog = Dog("Scooby")
cat = Cat("Carolina")
mouse = Mouse("Muse")
print(dog.name)
print(dog.is_Alive)
print(cat.name)
dog.speak()
cat.speak()
mouse.speak()