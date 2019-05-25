import datetime as dt


def datetime_deco(func):
    def decorated():
        print(dt.datetime.now())
        func()
        print(dt.datetime.now())
    return decorated


@datetime_deco
def mainfunc():
    print("----main ")


mainfunc()