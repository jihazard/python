
sentense = "i love you"

reverse = ""

for char in sentense:
    print(char ,"=====", reverse,"=====")
    reverse = char + reverse
    print(reverse)


print(reverse)