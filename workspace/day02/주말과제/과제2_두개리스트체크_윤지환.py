'''
과제2]
2 개 string 을 입력 받아 두글자 조합의 frequency 가 같은지 비교한다.
예,  (182, 281): true, 
     (34, 14): false, 
     (3589578, 5879385): true,  
     (22, 222): false
(해답) 조합의 frequency 가 같으려면 두 string 의 길이가 같고 글자들의 frequency 가 같아야 한다.

예)
sameFrequency('1233', '3133') --> not mached
sameFrequency('1233', '2133') --> mached

'''

def frequency_check(str1,str2):
    i = 0
    vali = Vali()
    # 길이체크 
    if vali.is_samelength(str1,str2):
        # 내용체크
        for n in str1:
            if str2.find(n) == -1:
                return print("not matched")    
        return print("matched") 
    else:
        return print("not matched")


class Vali:
    def is_samelength(self,str1,str2):
        try:
            if len(str1) == len(str2):
                return True
            else:
                return False
        except ValueError:
            return False
            
    def is_samecontent(self,a,b):
        try:
            if a != -1:
                return True
            else:
                return False
        except ValueError:
            return False


def main():
    print("==============================================")
    print("===============과제1 체크하기=================")
    a,b = "123377", "377321"
    frequency_check(a,b)
    print("==============================================")


if __name__ == "__main__":
    main()


