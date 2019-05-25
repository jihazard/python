# class Calculator:
#     result = 0

#     # def __init__(self):
#     #     sefl.result=0
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def plus(self):
#         self.result = self.x + self.y
#         return self.result


# calc = Calculator(1, 2)
# print(calc.plus())
# calc2 = Calculator(2, 2)
# print(calc2.plus())


class Person:
    name = ""
    age = 36

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def setName(self, name):
        self.name = name    


    def getName(self):
        return self.name    


    def job(self, job):
        print(self.name, self.age, job)


    # 정적메서드
    @staticmethod
    def isSquare():
        return True
    
    #클래스 메서드
    @classmethod
    def printCount(name):
        print("---------", name)


person = Person("윤지환", "30")
person.job("오징어")
print(person.name)
print(person.age)
