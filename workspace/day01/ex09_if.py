

flag = 0
while flag != 99 :
    var = int(input("정수를 입력하세요 "))
    if var > 0:
        if var % 2 == 0:
            print("{}는 양짝수입니다.".format(var))
        else:
            print("{}는 양홀수 입니다.".format(var))

    elif var == 0:
        print("{}는 0입니다.".format(var))
    else:
        if var % 2 == 0:
            print("{}는 음짝수입니다.".format(var))
        else:
            print("{}는 음홀수 입니다.".format(var))
    flag = var
