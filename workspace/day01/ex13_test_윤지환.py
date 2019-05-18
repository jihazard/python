'''
문제1 1~100까지 값 3배수의 합
문제2 평년과 윤년 판정프로그램

    year % 4 =0 :
    (year%100 !=0) | (year %400==0)
'''

print("--------------문제 1번")
sum =0;

for x in range(1,100,1) :
    if(x % 3==0) :
        sum += x
        print("배수의 값은 {} 입니다.".format(x))

print("3의 배수의 누적합은 {} 입니다. ".format(sum))


print("--------------문제 2번")

year = int(input("년도를 입력하세요"))

if year % 4 ==0 :
    if (year % 100 != 0 ) | (year % 400 ==0) :
        print("{}는 윤년입니다.".format(year))
    else :
        print("{}는 평년 입니다.".format(year))
else :
    print("{}는 평년 입니다.".format(year))
