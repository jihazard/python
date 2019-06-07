

def fibonacci(number):
    data = []
    for i in range(1, number+1):
        data.append(i)
    
    num = 1
    for x in data:
        print(x)
        if num >= 3:
            data[num] = data[num-1] + data[num-2]
           
        num += 1



def main():
    fibonacci(100)


if __name__ == "__main__":
    main()