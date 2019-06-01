import random

def range_pop():
    return random.randrange(1, 45)


if __name__ == "__main__":
    num = set([])
    while len(num) != 6:
        lotto = range_pop()
        num.add(lotto)
    print(num)

