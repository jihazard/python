import random

def get_number() :
    return random.randint(1,100)



def search_number(number,random_number):
    while(number is not random_number) :
            if number < random_number :
                print("정답은 {} 보돠 큽니다." .format(number))
            else :
                print("정답은 {} 보다 작습니다.".format(number))
            number = int(input("숫자를 입력하세요"))

def resultPrint(random_number):
    print("===============정답은 {} 입니다.============".format(random_number))

def main():
    print("searchNumber Program")
    print("============================")
    '''
    1. 랜덤숫자 만들기
    2. 숫자입력받기
    3. 출력하기
    '''
    random_number = get_number()
    print("숫자는 {} 입니다. " .format(random_number))
    print("숫자를 맞춰주세요 ~!")
    number = int(input("숫자를 입력하세요"))
    search_number(number,random_number)
    resultPrint(random_number)
    print("End of searchNumber Program")



if __name__ == "__main__":
    main()