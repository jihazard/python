def calc(values):
    sum = None

    try:
        sum = values[0] + values[1] + values[2]
    except IndexError as err:
        print("인덱스 에러 :", err)
    except Exception as err:
        print("에러 : ", err)
    else:
        print("에러업슴")
    finally:
        print(sum)


def main():
    calc([1, 2, 3, 6])
    calc([1, 2])


if __name__ == "__main__":
    main()