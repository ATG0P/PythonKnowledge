class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

c = Car("Tesla",2025,"White",True)
print(c.model)
print(c.year)
print(c.color)
print(c.for_sale)