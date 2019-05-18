#개떡같은 파이썬
* 파이썬 설치하기 
    - python.org
    - anaconda.com
    - IDE
        1. pycharm
        2. vscode
            - extension 설치 python , python for VScode 

* 파이썬 시작하기
    - 주석 
    ~~~python
    # 파이썬의주석처리

    ~~~
    - 데이터형식
        - Numbers
            - int , long , float , complex
        - String
            - '' , ""  ,+ , * , [] , [:]
        - List
            -  index : 0부터 전체 항목수에 -1 한것 까지 
        - Tuple(map)
            - (), [], [:] , index : 0부터 전체 항목수에 -1 한것 까지, *** readonly ***
        - Dicionary




    - 복소수 real , imag, conjugate(),abs()
    ~~~python
    a= 1+2j

    print(a.real) # 실수부분 3.0
    print(3-4j.real)
    print(a.imag) #허수부분
    print(3-4j.imag)
    print(a.conjugate()) #켤레 복소수
    print(3-4j.conjugate())
    print(abs(a)) # 복소수의 절대값
    print(abs(3-4j))
    ~~~


    - 문자형
    ~~~python
    str ="hello world"

    print(str)
    print(str[0])
    print(str[2:5])
    print(str[2:])
    print(str * 2)
    print(str  + "test")

    ~~~

    - 리스트 , 튜플
    ~~~python
    list =["abcd",765,2.22,"yoon",70.2]
    small=[123,456]

    print(list)
    print(list[0])
    print(list[1:3])
    print(list[2:])
    print(small *2)
    print(list + small)

    print("---------------------------------------")
    lst = [1,2,3,1,'abc',12.34,3]
    print(lst)
    lst.append("aaa")
    print(lst)
    lst.remove("aaa")
    print(lst)
    print(lst.count(1))
    print("---------------------------------------")
    t = (1,2,3,1,'abc',12.34,3)
    print(t)
    print(t.count(1))
    index = t.index(12.34)
    print(index)

    print(lst[1:4])
    print(type(t))
    print(type(lst))

    ~~~
    - 함수
        - str() 문자형으로 변환 ex) str(1) + 'hi '    '1hi'
        - type() 타입 확인  ex) type(1)    <class 'int'>   type('hello') <class 'str'>
        - strip() trim() 같이 사용
        - lower() , upper()
        - replace()
        - split()
        - input()  ex) x= input()         print("안녕하세요 " ,  x ) : 안녕하세요 x
 
* 