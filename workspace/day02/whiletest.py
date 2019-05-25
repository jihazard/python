def getStarNumber():
    return input("별 갯수를 입력하세요~ : ")

def makeStar(getvalue):
    number = int(getvalue)
    for num in range(1,number + 1 ):
        for x in range(1,num+1):
           print( "*" ,end='')
        print("")

def makeStarWhile(getvalue):
    number = int(getvalue)
    i = 0 
    while True:
        while i == i+1:
            print("*" , end="")
            if i == number : break
    i+=1
    print("")

def main():
    print("======================================")
    print("================while 문제=============")
    getValue = getStarNumber();
    makeStarWhile(getValue)
    
    
    print("================종료\\\\\\=============")


if __name__ == '__main__':
    main()
    