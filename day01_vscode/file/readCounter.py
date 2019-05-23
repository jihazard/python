f = open("yesterday.txt","r")

lyric = ""

while 1:
    line = f.readline()
    if not line:
        break
    lyric = lyric + line.strip() + "\n"
f.close()
totalnumber = lyric.upper().count("YESTERDAY")
yesterday1 = lyric.count("Yesterday")
yesterday2 = lyric.count("yesterday")


print("number of word Yesterday : " , totalnumber) 
print("Yesterday : {} \nyesterday : {}".format(yesterday1,yesterday2))
