class Maxym:
    def __init__(self, name: str = None, birth: int = 2007, surname: str = None):
        self.name = name
        self.surname = surname
        self.__birth = birth
    def calculate(self, current_year: int):
        if self.__birth == None:
            return None
        course = current_year - (self.__birth + 15)
        return course
    def listik(self):
        return [self.name, self.surname]

class PlayDota2(Maxym):
    def __init__(self, name: str, surname: str, birth: int, put_wards: bool, farm_gold: bool, ruin: bool):
        super().__init__(name, surname)
        self.__birth= birth
        self.put_wards = put_wards
        self.farm_gold = farm_gold
        self.ruin = ruin
        self._mmr = 0
    
    def role(self):
        if self.put_wards and not self.farm_gold:
            print("Support terpila)))")
            return "sup"
        elif self.farm_gold and not self.ruin:
            print("Solo 1x9")
            return "carry"
        elif not self.farm_gold and self.ruin and self.__birth > 2010:  
            print("typa prishchepka")
        else:
            print("norm tipok")

    def input_bf_time(self):
        time = int(input("When u take bf: "))
        if time < 15 and self.role() == "carry":
            print("joskiy")
        elif time > 15 and self.role() == "carry":
            print("noob")
        elif self.role() == "sup":
            print("nah tobi bf?")

    def mmr_rank(self, mmr: int):
        self._mmr = mmr 
        if mmr < 1000:
            print("Herald")
        elif mmr < 2000:
            print("Guardian")
        elif mmr < 3000:
            print("Crusader")
        elif mmr < 4000:
            print("Archon")
        elif mmr < 5000:
            print("Legend")
        elif mmr < 6000:
            print("Ancient")
        else:
            print("Divine/Immortal")

obj = Maxym("Maxym", "Bogulskyi")
obj1 = Maxym("Vitaly")
course = obj1.calculate(2025)
name_list = obj1.listik()

sapik = PlayDota2(name= "Maxym", birth= 2011 ,surname= "Bogulskyi", put_wards= False, farm_gold= True, ruin= False)
sapik.role()
sapik.input_bf_time()


# print(f"U are now at +- {course} course")
# print(name_list)
