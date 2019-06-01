
def userInput(listx, num):
    print(num, "개의 정수를 입력하세요!")

    for i in range(num):
        su = int(input("integer input :"))
        listx.append(su)


def userOutput(listx, num):
    for i in range(num):
        print("{} 번째 정수 ==> {}".format(i, listx[i]))


def userHap(listx, num):
    sum = 0
    for i in range(num):
        sum += listx[i]
        print(listx[i], end=' ')

    print("totam sum :", sum)