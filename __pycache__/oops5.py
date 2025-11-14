class Animal:
    def __init__(self,name):
        self.name = name
    def sleep(self):
        print(f"{self.name} is sleeping")
    def eat(self):
        print(f"{self.name} is eating")

class Prey(Animal):
    def flee(self):
        print("this animal will flee")

class Predetor(Animal):
    def attack(self):
        print("this animal will atack")

class Rabbit(Prey):
    pass

class Hawk(Predetor):
    pass

class Fish(Predetor,Prey):
    pass

rabbit = Rabbit("sasa")
hawk = Hawk("gidad")
fish = Fish("machli")
hawk.attack()
hawk.sleep()