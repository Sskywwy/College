class Maxym:
    def __init__(self, name: str = None, surname: str = None, birth: int = None):
        self.name = name
        self.surname = surname
        self.birth = birth
    
    def calculate(self, current_year: int):
        if self.birth == None:
            return None
        course = current_year - (self.birth + 15)
        return course
    def listik(self):
        return [self.name, self.surname]


obj = Maxym("Maxym", "Bogulskyi", 2007)
obj1 = Maxym("Vitaly", birth=2010)
course = obj1.calculate(2025)
name_list = obj1.listik()

print(f"U are now at +- {course} course")
print(name_list)