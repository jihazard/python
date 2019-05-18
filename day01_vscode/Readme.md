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
        - Tuple
            - (), [], [:] , index : 0부터 전체 항목수에 -1 한것 까지, *** readonly ***
        - Dicionary(map)
            - {} , 해시 테이블의 일종,  키-값 쌍으로 구성 
        - Set
            - {} , 중복허용 안함, 순서가 없음, 인덱싱을 통해 자료형의 값 획득 불가능

        - 집합 자료형 활용
            - 교집합 (&, intersection()) ex)  a1 & b1  ,  a1.intersection(b1)
            - 합집합 (| , union())  ex) a1 | b1 , a1.union(b1)
            - 차집합 (- , difference()) ex) a1 - b1 , a1.dirrence(b1)


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
    -dictionary
    ~~~python
    dict={}

    dict["one"] = "this is one"
    dict[2] = "this is two"

    tinydict = {'name': 'john', 'code': '1234', 'room': 123}

    print(dict["one"])
    print(dict[2])
    print(tinydict)
    print(tinydict["name "])

    ~~~

    - set
    ~~~python
    s=set([1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])

    print(s) #중복불가
    s2 = set("happy jihwan")
    print(s2)

    s2.add("111")
    print(s2)
    s2.update({"korea", "usa", "japan"})
    print(s2)

    s2.remove("japan")
    print(s2)

    s2.discard("usa")
    print(s2)

    print(s2)

    s2.clear();
    print(s2)
    ~~~

    - 집합 자료형 활용 
    - 함수
        - str() 문자형으로 변환 ex) str(1) + 'hi '    '1hi'
        - type() 타입 확인  ex) type(1)    <class 'int'>   type('hello') <class 'str'>
        - strip() trim() 같이 사용
        - lower() , upper()
        - replace()
        - split()
        - input()  ex) x= input()         print("안녕하세요 " ,  x ) : 안녕하세요 x
 
* 