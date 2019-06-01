
def hap(a, b):
    return a + b


def safe_hap(a, b):
    if type(a) != type(b):
        print("타입이 달라서 더 할수 없습니다.")
        return 
    else:
        result = hap(a, b)
        return result