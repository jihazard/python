import sys

def fileWrite():
    with open("examplefile.txt", 'w') as file:
        data = file.write("에헤헤ㅔ헤헤헤헤헤헤헤헤헤헿헤헤")

    try:
        f= open("examplefile.txt1", "r")
        text = f.read()
        print(text)
        f.close()
    except IOError as err:
        print("ioerror", err)
        sys.stderr.write("file read err")
    else:
        pass
    finally:
        pass


def main():
    fileWrite()

if __name__ == "__main__":
    main()