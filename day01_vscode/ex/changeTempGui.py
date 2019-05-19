import easygui

choices = ["1.화씨 섭씨 변환", "2.섭씨 화씨 변환","3.종료"]
menu =0;
while menu != 3 : 
    select = easygui.choicebox("온도 변환 메뉴 선택 " , choices=choices)
    print(select)
    if select != 'None' :
        menu = select.split(".")
        menu = menu[0]
        menu = int(menu)
        print(" 입력받은 메뉴 ==> {} ".format(menu))
        if menu == 1 :
            fahr= easygui.integerbox("화씨 온도 입력")
            cal = 5* (float(fahr)  - 32 ) / 9
            print("섭씨 온도  : {}".format(cal))
            easygui.msgbox("섭씨 온도는 {} 입니다.".format(cal))

        elif menu == 2 :
            fahr= easygui.integerbox("섭씨 온도 입력")
            cal = float(fahr) * 9 / 5  + 32
            print("화씨 온도  : {}".format(cal))
            easygui.msgbox("화씨 온도는 {} 입니다.".format(cal))

        elif menu == 3 :
            print("종료합니다.")
            easygui.msgbox("종료합니다.")


        else :
            easygui.msgbox("잘못입력했습니다.")
