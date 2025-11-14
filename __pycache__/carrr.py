class Sar:
    a = 10 #class variable
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color  #instance variables
        self.for_sale = for_sale
    def mad(self):
        print(f"You are mad if you think you can drive {self.color} {self.model}")
    def describe(self):
        print(f"{self.model}, {self.year}, {self.color}, {self.for_sale}")