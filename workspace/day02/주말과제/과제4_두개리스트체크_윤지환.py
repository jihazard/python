'''
과제4]
파이썬 강좌의 수강생 목록은 다음과 같다. 어떤 사람이 수강생 목록에 존재하는지
    check 하는 함수를 작성하라.(함수명 임의적으로 생성)
    목록에 존재하면 True, 존재하지 않으면 False 를 반환한다.

   students = ["김철수", "홍길동", "문재인", "김정은", "트럼프", "성춘향"]

  결과 출력 예상>
   print(check_list(students, "홍길동")) 


'''

def check_list(database,findPerson):
    return True if findPerson in database else False

def main():
    print("==============================================")
    print("===============과제4 수강생목록  =============")
    students = ["김철수", "홍길동", "문재인", "김정은", "트럼프", "성춘향"]
    print(check_list(students,"김정은"))
    
    print("==============================================")


if __name__ == "__main__":
    main()


