


class Emp:
    dataList = []  

    def addDatabase(self, name, no, dept, tel, price):
        info = {
                "이름": name,
                "부서": dept,
                "사번": no,
                "연락처": tel,
                "월급": price
              }
        self.dataList.append(info)

    def getDatalist(self):
        return self.dataList


class Regular(Emp):
    def __init__(self, dataList):
        self.dataList = dataList
          
    # 급여 
    def priceAll(self):
        print("==========월급===================================")
        for info in self.dataList:
            price = int(info.get("월급")) 
            print("{} price : {} 원".format(info.get("이름"), price))
        
    def priceOne(self, no):
        print("==========월급===================================")
        for info in self.dataList:
            if no == info.get("사번"):
                price = int(info.get("월급")) 
                print("{}  price: {} 원".format(info.get("이름"), price))
        


class Sales(Regular):
    # 커미션
    def commissonAll(self):
        commi = 1.2
        print("==========커미션===================================")
        for info in self.dataList:
            price = int(info.get("월급")) * commi
            print("{} commisson : {} 원".format(info.get("이름"), price))


def main(): 
    print("===================================================")
    emp = Emp()
    emp.addDatabase("윤지환", 1, "그냥사업부", "010", 100000)
    emp.addDatabase("김득현", 2, "개발사업부", "010", 200000)
    emp.addDatabase("박기두", 3, "노동사업부", "010", 300000)
    emp.addDatabase("노경주", 4, "우리사업부", "010", 400000)
    re = Regular(emp.dataList)
    re.priceOne(1)
    sa = Sales(re)
    flag = 999;

    while flag != 6:
        print("================월급 입력하세요 ===============")    
        print("========1.회원 전체 조회 2. 월급 전체 조회 3. 월급 조회 4.커미션 전체 조회 5. 커미션조회 6.종료")
        flag = int(input("번호를 입력해주세요"))
        if flag == 1:
            pass
        elif flag == 2:
            re.priceAll()
        elif flag == 3:
            name = int(input("검색할 사원 번호를 입력해주세요 :: "))
            re.priceOne(name)
        


       
    print("===================================================")

if __name__ == "__main__":
    main()
