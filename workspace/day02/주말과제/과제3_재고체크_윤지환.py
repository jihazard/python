'''
과제3]
상점의 모든 과일의 재고와 전체 가격 계산
각 과일의 개당 가격은 다음과 같다.

바나나 : 4000 원
사과: 2000 원
오렌지: 1500 원
배 : 3000 원

각 과일의 재고는 다음과 같다.
바나나 : 6 개
사과 : 0 개
오렌지: 32 개
배 : 15 개

dictionary 를 이용하여 재고 과일의 총 금액을 계산하라. 
(가격 dictionary 와 재고 dictionary 를 별도로 작성)

예상 output:

price: 4000
stock: 6
price: 2000
stock: 0
price: 1500
stock: 32
price: 3000
stock: 15
The total money is 117000

'''

def cal(prices,counts):
    totalmoney = 0
    for name in prices:
        print("price: {} \nstock: {}".format(prices.get(name),counts.get(name)))
        totalmoney += prices.get(name) * counts.get(name)
    print("The total money is {}".format(totalmoney))



def main():
    print("==============================================")
    print("===============과제3 재고체크하기=============")
    prices = {"바나나": 4000, "사과": 2000, "오렌지": 1500, "배": 3000}
    counts = {"바나나": 6, "사과": 0, "오렌지": 32, "배": 15}
    cal(prices,counts)
    
    print("==============================================")


if __name__ == "__main__":
    main()


