

a= 1+2j

print(a.real) # 실수부분
print(3-4j.real)
print(a.imag) #허수부분
print(3-4j.imag)
print(a.conjugate()) #켤레 복소수
print(3-4j.conjugate())
print(abs(a)) # 복소수의 절대값
print(abs(3-4j))


str ="hello world"

print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str  + "test")

list =["abcd",765,2.22,"yoon",70.2]
small=[123,456]

print(list)
print(list[0:1])
print(list[1:3])
print(list[2:])
print(small *2)
print(list + small)


print("---------------------------------------")
lst = [1,2,3,1,'abc',12.34,3]
print(lst)
lst.append("aaa")
print(lst)
lst.remove("aaa")
print(lst)
print(lst.count(1))
print("---------------------------------------")
t = (1,2,3,1,'abc',12.34,3)
print(t)
print(t.count(1))
index = t.index(12.34)
print(index)
print("hi" + str(3))


print("hi" + str(333))