def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    '''
    연속배열 삭제 하기

    '''
    result = []
    i = 0;
    for num in arr:
        print(num)
        print("indexing :" , arr[i])
        temp = 0
        if i > 0: 
            print("이전값 : {} , 현재값 : {}".format(arr[i-1] ,num))
            
            if arr[i-1] == num:
                print("delet index : ", arr[i-1])
                answer.remove(i-1)    
    i+=1 
            
    return answer




def main():
    arr = [1, 1, 3, 3, 0, 1, 1]
    print(solution(arr))


if __name__ == "__main__":
    main()
