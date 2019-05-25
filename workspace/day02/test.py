def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x/y


def calc2(a, b, key):
    
    if key == "*":
        return a*b
    elif key == "+":
        return a+b 
    elif key == "-":
        return a-b
    else:
        return a/b 


def calc3(a, b, key):
    cals = {"add": add(a, b), "minus": sub(a, b), "mul": mul(a, b), "div": div(a, b)}
    print(cals.get(key))


def calc4(a, b, key):
    cals = {"add": (lambda a, b: a + b)(a,b), "minus": (lambda a, b: a - b)(a,b), "mul": (lambda a, b: a * b)(a,b) }
    print(cals.get(key))


def main():
    calc4(1, 2, "mul")


if __name__ == "__main__":
    main()