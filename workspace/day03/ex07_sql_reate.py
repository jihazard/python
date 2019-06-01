import sqlite3 as s




#디비연결
conn = s.connect('kosmoDB.db')
c = conn.cursor()

c.execute("drop table if exists menupan")
c.execute('create table menupan(menu char(20), price int)')

print("======생성")
print(conn)
c.execute('insert into menupan values("김밥", 3000)')
c.execute('insert into menupan values("순두부", 7000)')
c.execute('insert into menupan values("육계장", 6500)')

conn.commit()

c.execute('select * from menupan')
rows = c.fetchall() #fetchone()


for row in rows:
    print(row)

c.close()
conn.close()