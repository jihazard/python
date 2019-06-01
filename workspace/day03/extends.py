
class HousePark:
    lastname = "park"

    def __init__(self, name):
        self.fullName = self.lastname + name

    def travel(self, where):
        print("{} {} 여행을 가다.".format(self.fullName, where))

    def love(self, other):
        print("{} {} 사랑하다.".format(self.fullName, other.fullName))
    
    def __add__(self, other):
        print("{} {} 결혼".format(self.fullName, other.fullName))
    

class HouseLee(HousePark):
    lastname = "lee"
 
    def travel(self, where, day):
        print("{} {} {}여행을 가다.".format(self.fullName, where, day))


mysub = HouseLee("자손")
mysub.travel("방콕", "5일")

parent = HousePark("지환")
child = HouseLee("아들")

parent.love(child)
parent + child



