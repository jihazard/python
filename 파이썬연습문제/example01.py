def solution(arr):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    i = 0
    temp = []
    for num in arr:
        if i > 0: 
            if arr[i-1] == num:
               # arr[i] = "x"
                temp.remove(arr[i])
           
                
        i += 1 
        print(arr)
        print(temp)
     
    return arr


def main():
    arr = [4, 4, 4, 3, 3]
    print(solution(arr))


if __name__ == "__main__":
    main()
