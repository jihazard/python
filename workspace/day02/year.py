import datetime


def main():
    now = datetime.datetime.now()
    today = now.timetuple()
    print(now, "///", today)
    year = today[0]
    print(year)
    tear2 = today.tm_year
    print(tear2)
    tear3 = now.today()
    print(tear3)
    tear4 = now.weekday()
    print(tear4)
    
    tear5 = now.isoformat(sep='T', timespec='auto')
    print(tear5)



if __name__ == "__main__":
    main()