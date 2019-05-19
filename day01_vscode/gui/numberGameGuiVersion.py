import easygui
import random

num = 0

times = 6
answer = random.randint(1,100)

while num != answer and times > 0 :
    num = easygui.integerbox("1~100 사이 숫자를 입력하세요 . 도전기회 = " + str(times))
    if num < answer : 
        easygui.msgbox(str(num)  + " 은 정답보다 큽습니다.")
    else :
        easygui.msgbox(str(num) + " 은 정답보다 작습니다.")
    
    times -= 1


if num == answer :
    easygui.msgbox(" 정답입니다. 정답은 {} 입니다. ".format(answer))
else :
    easygui.msgbox(" 실격입니다. 정답은 {} 입니다.".format(answer))