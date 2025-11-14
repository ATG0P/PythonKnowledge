class Books:
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.name} : {self.author}, {self.pages}"
    def __eq__(self, other):
        return self.name == other.name and self.author == other.author
    def __lt__(self,other):
        return self.pages<other.pages
    def __gt__(self,other):
        return self.pages>other.pages
    def __add__(self,other):
        return self.pages+other.pages
    def __contains__(self,keyword):
        return keyword in self.name or keyword in self.author
    def __getitem__(self,key):
        if key == "name":
            return self.name
        elif key == "author":
            return self.author
        elif key=="no of pages":
            return self.pages
        else:
            return "Invalid request"
        
book1 = Books("Harry Potter","J.K Rowling",300)
book2 = Books("Atomic Habits","James Clear",320)
book3 = Books("The Monk who sold his ferrari","Robin Sharma",280)
book4 = Books("Atomic Habits","James Clear",320)
print(book1)#due to __str__ function
print(book2 == book4)#due to __eq__ function
print(book1>book2)#__lt__
print(book2>book3)#__gt__
print(book1+book2)#__add__
print("Habits" in book2)#__contains__
print(book1["author"])#__getitem__