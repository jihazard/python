list = ["서울","도쿄","파리","베를린"]

print(list)

list.append("상파울로")
print("추가 => {}".format(list))
list.remove("서울")
print("삭제 => {}".format(list))

list.reverse()
print("전환정렬 => {}".format(list))
list.sort()
print("순차정렬 => {}".format(list))
