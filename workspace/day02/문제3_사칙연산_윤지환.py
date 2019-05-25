class FourCal:
      
    def plus(self, *args):
        result = 0
        for n in args:
            result += n
        return result    

    def sub(self, *args):
        result = 0
        for n in args:
            result -= n
        return result  

    def mul(self, *args):
        result = 1
        for n in args:
            result *= n
        return result  

    def div(self, *args):
        result = 1
        for n in args:
            result /= n
        return result  


class FourCal2:
      
    def plus(self, *args):
        return sum(args)    

    def sub(self, *args):
        result = 0
        for n in args:
            result -= n
        return result  

    def mul(self, *args):
        result = 1
        for n in args:
            result *= n
        return result  

    def div(self, *args):
        result = 1
        for n in args:
            result /= n
        return result  


cal = FourCal()
plus = cal.plus(1, 2, 3, 4, 5)
print(plus)
sub = cal.sub(1, 2, 3, 4, 5)
print(sub)
mul = cal.mul(1, 2, 3, 4, 5)
print(mul)
div = cal.div(1, 2, 3, 4, 5)
print(div)