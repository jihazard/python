

print("--------------온도변환 메뉴 ---------------")
print("--------------1.화씨 섭씨 변환 메뉴--------")
print("--------------2.섭씨 화씨 변환 메뉴--------")
print("--------------3.종료 ---------------------")


menu  = 0 

while menu != 3 : 
    menu = int(input("메뉴를 선택해주세요 "))
    if menu == 1 :
        fahr = float(input("화씨 온도 입력 : "))
        cal = 5* (fahr  - 32 ) / 9
        print("섭씨 온도  : {}".format(cal))

    elif menu == 2 :
        fahr = float(input("섭씨 온도 입력 : "))
        cal = fahr * 9 / 5  + 32
        print("화씨 온도  : {}".format(cal))

    elif menu == 3 :
        print("종료합니다.")

    else :
        print("잘못입력했습니다.")