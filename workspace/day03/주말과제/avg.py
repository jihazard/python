
def average(listx):
    total = 1
    for num in listx:
        total *= num
    
    return total
    

def main():
    list = [2,3,4,5,6]
    print(average(list))



if __name__ == "__main__":
    main()


