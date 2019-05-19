
def read_file() : 
    print("------")
    f= open('temp.txt')
    
    while True : 
        line = f.readline()
        if len(line) == 0 :
            break
        line = line.strip()
        mymemo.append(line)

    f.close()



mymemo = []

read_file()

for item in mymemo :
    msg = item + '\n'
    print(msg)