
def f(i, list):
    i += 1
    list.append(0)


def cal(i, j, factory=1):
    return i * j * factory


def f2(i, list):
    i += 1
    list.append(0)
    return i, list


def total(*numbers):
    tot = 0
    for n in numbers:
        tot += n
    return tot


def calc(*numbers):
    count = 0
    tot = 0

    for n in numbers:
        count += 1
        tot += n
    return count, tot


def funcs(arg1, arg2, arg3, *args):
    print("arg1 : {} \narg2 : {} \narg3 : {}\nargs : {}\n".format(arg1, arg2, arg3, args))


def poptest(list, pops):
    for x in pops:
        print(list, "//", x)
        list.pop(x)
    return list


def totals(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count


def sample(a, *args, **kwargs):
    print("a : {} \nargs : {} \nkwargs : {}".format(a, args, kwargs))


def print_function(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    print(type(kwargs))

    for name, value in kwargs.items():
        print(name, value)


def print_args(*args):
    print(args)
    print(args.count(2))
    print(type(args))


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
    cals = {"add": (lambda a, b: a + b)(a, b), "minus": (lambda a, b: a - b)(a, b), "mul": (lambda a, b: a * b)(a,b) }
    print(cals.get(key))


def main():
    calc4(1, 2, "mul")
   
    # print_args(1, 2, 3, 4)
    # print_function(a="1", b="2", c="3")

    # sample(1, 2, 3, 4, 5, x="50", b="100")
    # print(totals(10, 1, 2, 3, veg=50, fru=100))

    # f = total(1, 2, 3, 4)
    # print(f)

    # count, sum = calc(1, 23, 4, 5, 6)
    # print(count, sum)

    # list = [1, 2, 3, 4, 5]
    # pops = [0, 1, 2]

    # print(poptest(list, pops))
    # k = 10  # k는 immutable
    # m = [1, 2, 3]  # mutable
    # f(k, m)
    # print(k, m)

    # result = cal(10, 20)
    # print(result)

    # func = f2(k, m)
    # print(func[0], func[1])
    # print(func.index)
    # print(func.__getitem__)
    # print(func.count)
    

if __name__ == "__main__":
    main()