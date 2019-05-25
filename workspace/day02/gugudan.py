def getStarNumber():
    return input("단수를 입력하세요~ : ")


def printGugudan(getValue):
    number = int(getValue)
    for i in range(number, 9, 1):
        for j in range(1, 9, 1):
            print("{0:>3d} * {1:>3d} = {2:>3d}".format(i, j, j * i), end="")
        print("")


def printGugudanVer2(getValue):
    for i in range(2, 9, 1):
        for j in range(1, 9, 1):
            print("{0:>3d} * {1:>3d} = {2:>3d}".format(i, j, j*i), end="")
        print("")

        
def main():
    print("======================================")
    print("================gugudan 문제=============")
    getValue = getStarNumber()
    printGugudanVer2(getValue)
    print("================종료\\\\\\=============")


if __name__ == '__main__':
    main()
    