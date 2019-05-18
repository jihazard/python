inputs = input("학점을 입력하세요 ")

score = inputs.split(",")
sum1 = 0

for x in score:
    sum1 += int(x)

su = sum1 / len(score)

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

print("점수는 {}점 학점은 {} 입니다.".format(su, result))
