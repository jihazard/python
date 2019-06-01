import random


class Dice:
    def getDice():
        return random.randint(1, 6)


class Unit:
    def __init__(self, name, hp, exp):
        self.name = name
        self.job = __class__.__name__
        self.hp = hp
        self.exp = exp

    def getUnitInfo(self):
        print("이름 : {}\n직업 : {}\nHP : {}\n exp : {}".format(self.name, self.job, self.hp, self.exp))

    def attack(self, other, damage):
        if dice > 3:
            print("{}가 {}에게 {}데미지 공격 성공".format(self.name, other.name, damage))
            other.hp-damage

        else:
            print("{}가 {}에게 {}데미지 공격 실패".format(self.name, other.name, damage))

    
    def defence(self):
        pass


    def status(self):
        if self.hp == 0:
            print("사망")
        


class Knight(Unit):
    pass


class Enemy(Unit):
    pass


class Battle(Knight, Enemy):
    pass


def main():
    dice = Dice.getDice()
    hero = Knight("기두", 100, 100)
    enemy = Enemy("고블린", 100, 10)
    print(dice)
    print(hero.getUnitInfo())
    print(enemy.getUnitInfo())


if __name__ == "__main__":
    main()