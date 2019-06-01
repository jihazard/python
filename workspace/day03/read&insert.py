import sqlite3 as s


conn = s.connect('kosmoDBaddress.db')
cursor = conn.cursor()

cursor.execute("drop table if exists student")
cursor.execute("create table student(name char(20), kor int, eng int, math int, total int, avg int)")

query = 'insert into student (name, kor, eng, math ,total,avg) values(?, ?, ?, ?, ?, ?)'

arr = []
with open("D:/python/read/score.txt", "r") as f:
    for info in f:
        arr = info.split(" ")
        total = int(arr[1])+int(arr[2]) + int(arr[3])
        avg = total/3
        # print("{}  {}  {}  {}  {}  {}".format(arr[0], arr[1], arr[2], arr[3], total, avg))
        cursor.execute(query, (arr[0], arr[1], arr[2], arr[3], total, avg))

conn.commit()
cursor.execute("select * from student")
rows = cursor.fetchall()

for row in rows:
    print(row)



cursor.execute('select * from student where name= "김연아"')
rows = cursor.fetchall()
print("search result ===== > {}".format(rows))