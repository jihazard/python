f = open("test2.txt", "w")  # write
# f = open("test2.txt", "r") # read

for i in range(1,11):
    data = "%d번째 줄입니다. \n" % i
    print(data)
    f.write(data)

f.close()


while 1: 
    data = input("input : ")
    if not data:
        break

    print(data)


f = open("test2.txt", "r") # read
lines = f.readlines()

# for line in lines:
#     print(line)

while True:
    data = f.readline()
    if not data: 
        break
    print(data)

f.close()
