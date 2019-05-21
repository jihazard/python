def get_dan_value() :
    return int(input("구구단 몇단을 계산할까요? : "))

def calculateGugudan(dan):
        for j in range(1,10,1) :
            print("{0:>3d}  * {1:>3d}  = {2:>3d}".format(dan,j,dan*j))
    

def main():
    print("gugudan Program")
    print("============================")
    '''
    1. 단입력받기
    2. 출력하기
    '''
    get_dan = get_dan_value()
    print("구구단 {} 단을 계산합니다. " .format(get_dan))
    calculateGugudan(get_dan)
    print("===========================")
    print("End of gugudan Program")

if __name__ == '__main__':
    main()

