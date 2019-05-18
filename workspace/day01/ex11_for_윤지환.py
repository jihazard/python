'''
    for 변수 in 리스트(튜플,문자열) :
    수행문자 1
    수행문자 2

'''

dan = int(input("단 "))

for i in range(1, 10, 1):
    print("{} * {} = {}".format(dan,i,dan*i))