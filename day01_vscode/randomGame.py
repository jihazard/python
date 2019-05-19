import random

answer  = random.randint(1,100)

print(answer)

num = 0
times = 6


while num != answer and times > 0 :
    num = int(input("값을 입력하세요 >>> "))
    if num < answer :
        print("정답보다 작습니다.")
    else :
        print("정답보다 큽니다.")
    
    times = times - 1
    print("{} 번 기회가 남았습니다.".format(times))
    print()


if num == answer :
    print("정답입니다.")

else :
    print(" 탈락입니다 정답은 {} 입니다 : ".format(answer))