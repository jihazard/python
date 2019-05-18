# 이름 , 국어, 영어, 전산 점수 입력받기 문제 성적구하기

inputs = input("이름,국어,영어 전산 점수를 , 입력하세요 ")

score = inputs.split(",")
sum1 = 0
print(score[1:])

for x in score[1:]:
    sum1 += int(x)

su = sum1/(len(score)-1)

if su >= 90:
    result = "A"
elif su >= 80:
    result = "B"
elif su >= 70:
    result = "C"
elif su >= 60:
    result = "D"
else:
    result = "F"

print("이름은 {} 점수는 {}점 평균은 {:.2f} 학점은 {} 입니다.".format(score[0],sum1,su, result))



