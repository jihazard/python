import sqlite3 as s



#디비연결
conn = s.connect('kosmoDBaddress.db')
c = conn.cursor()

c.execute("drop table if exists address")
c.execute('create table address(name char(20), phoneNumber char(100))')

print("======생성")
print(conn)
c.execute('insert into address values("윤지환", datetime("now","localtime"))')
c.execute('insert into address values("박기두", "010-2931-2956")')
c.execute('insert into address values("노경주", "010-2931-2955")')

conn.commit()

c.execute('select * from address')
rows = c.fetchall() #fetchone()

print(rows)

for row in rows:
    print(row)

c.close()
conn.close()