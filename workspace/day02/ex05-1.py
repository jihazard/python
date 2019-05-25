def print_func(a, b, c):
    print(a, b, c)
    print(a, b)
    print(a )


def main():
    print_func(1, 2, 3)
    p = ['k', 'b', 's']
    print_func(*p)

    p2 = {"c": "1", "a": "2", "b": "3"}
    print_func(**p2)

if __name__ == "__main__":
    main()