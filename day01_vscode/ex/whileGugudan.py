def get_dan_value() :
    return int(input("구구단 몇단을 계산할까요? : "))

def printGuguDAN() :
    get_dan = get_dan_value()  
    while get_dan is not 0 :
        print("단  {}".format(get_dan))
        for i in range(1,10,1) :
            print( "{0:>3d} * {1:>3d} = {2:>3d}".format(get_dan,i,get_dan*i))
        get_dan = get_dan_value()  
     


def main() :
    print("=========gugudan game ========")
    print("===================== ========")
    
    get_dan = 1
    
    while get_dan is not 0 :
        print("단  {}".format(get_dan))
        for i in range(1,10,1) :
            print( "{0:>3d} * {1:>3d} = {2:>3d}".format(get_dan,i,get_dan*i))
        get_dan = get_dan_value()

    '''
    1. 단 받기
    2.  출력
    3. 다시 단받기
    '''

if __name__ == "__main__":
    main()