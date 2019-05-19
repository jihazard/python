import easygui

choices = ["김밥", "비빔밥","떡볶이"]

reply = easygui.choicebox("무엇을 드시겠습니까?" , choices=choices)
easygui.msgbox(reply +" 을 주문했습니다.")