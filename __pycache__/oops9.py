class Animals():
    alive = True

class Dog(Animals):
    def speak(self):
        print("WOOF!")

class Cat(Animals):
    def speak(self):
        print("MEOW!")

class Car:
    alive = False
    def speak(self):
        print("HONK!")

animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)