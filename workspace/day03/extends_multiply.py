class PersonOne:
    def __init__(self):
        self.one = 1 


class PersonTwo:
    def __init__(self):
        self.two = 2


class Child(PersonOne, PersonTwo):
    def __init__(self, one, two, three):
        # super().__init__()
        PersonOne.__init__(self)
        PersonTwo.__init__(self)
        self.three = three


child = Child(1, 2, 3)
print(child.__dict__)


class Unit:
    def __init__(self, name,  hp, exp):
        self.name = name
        self.job = self.__class__.__name__
        self.hp = hp
        self.exp = exp

    def getUnitInfo(self):
        print("이름 : {}\n직업 : {}\nHP : {}\n exp : {}".format(self.name, self.job, self.hp, self.exp))


class Knight(Unit):
    pass


knight = Knight("기두", 100, 10)
knight.getUnitInfo()
