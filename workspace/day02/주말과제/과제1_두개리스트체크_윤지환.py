'''
과제1]
-첫번째 list 와 두번째 list 의 length 는 동일
-두번째 list 의 각 element 는 첫번째 list element 의 제곱이어야 한다.
-서로 match 되는 element 가 위 조건과 같은지 비교하여 
   참이면 "Two lists are matched", 
   거짓이면 "Two lists are unmatched" 출력
예)
frequency_check([1,2,3,2,5,6], [1,4,9,4,25,36]) --> lists are matched

'''

def frequency_check(list_a,list_b):
    i = 0
    for n in list_a:
        if is_true(n,list_b[i]):
            return print("Two lists are unmatched")
        i += 1
    return print("lists are matched")


def is_true(a,b):
    try:
        if a**2 != b:
            return True
        else:
            return False
    except ValueError:
        return False


def main():
    print("==============================================")
    print("===============과제1 체크하기=================")
    a,b = [1,2,3,2,5,6], [1,4,9,4,25,369]
    frequency_check(a,b)
    print("==============================================")


if __name__ == "__main__":
    main()


