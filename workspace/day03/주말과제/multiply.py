'''
5) 임의의 범위의 숫자를 모두 곱하는 함수를 작성하라.
    ex) multiply(2,4) ==> 2 * 3 * 4 = 24
'''

def multiply(startNum, endNum):
    multi = 1;
    for i in range(startNum, endNum + 1):
        multi *= i

    return multi


def main():
    print(multiply(2, 4))


if __name__ == "__main__":
    main()