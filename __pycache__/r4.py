class Studentsofdjs:
    def __init__(self,name):
        self.name = name
class Gender(Studentsofdjs):
    def Male(self):
        print(f"{self.name} is male")
    def Female(self):
        print(f"{self.name} is female")


class Durva(Gender):
    def hobby(self):
        print(f"{self.name} loves to dance")
class Aryan(Gender):
    def hobby(self):
        print(f"{self.name} loves to play football")
class Shreyas(Gender):
    def hobby(self):
        print(f"{self.name} loves to play Valorant")
s1 = Durva("Durva")
s2 = Aryan("Aryan")
s3 = Shreyas("Shreyas")