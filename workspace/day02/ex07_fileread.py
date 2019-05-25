

# f = open("D:\\python\\python\\read\\sample.txt", "w+")
f = open("D:/python/python/read/sample.txt", "r+")


while True:
    l = f.read()
    if not l: 
        break
    print(l)

f2 = open("D:/python/python/read/sample.txt", "r+")
readLine = f2.read()

for line in readLine:
    print(line, end="")

f2.close()


with open("D:/python/python/read/sample.txt", "w") as f3:
    f.write("life is too short")


with open("d:/test.txt",'a') as f4:
    for i in range(21,40):
        data = "{} 번째 줄입니다.".format(i)
        f4.write(data)

print("test.txt 어펜드 추가완료")

'''
\문자 : 제어문자
 \n , \t
 경로 - \\ => \
'''

