
print("-------dictionary==========================")

dict={}

dict["one"] = "this is one"
dict[2] = "this is two"

tinydict = {'name': 'john', 'code': '1234', 'room': 123}

print(dict["one"])
print(dict[2])
print(tinydict)



print("-------set==========================")

s=set([1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])

print(s) #중복불가
s2 = set("happy jihwan")
print(s2)

s2.add("111")
print(s2)
s2.update({"korea", "usa", "japan"})
print(s2)

s2.remove("japan")
print(s2)

print("000000")

print(s2)

s2.clear();
print(s2)



s1= set([1, 2, 3, 4, 5, 6])
s2= set([4, 5, 6, 7, 8, 9])

#교집합
print(s1 & s2)
print(s1.intersection(s2))
#합집합
print(s1 | s2)
print(s1.union(s2))
#차집합
print(s1-s2)
print(s1.difference(s2))







