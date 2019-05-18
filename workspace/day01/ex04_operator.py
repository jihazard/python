
print(7/3)
print(7%3)
print(7//3)
print(2**3)

x=4
y=7

print(4&7)  #4
print(4|7)  #7
print(4^7)  #3
print(~x)  #3
print(4<<7)
print(4>>7)


'''
보수 연산 
    ~  : - (원래값 +1 ) 
    
'''
print(~y) #-8
print(~100) #-101
print(~-100) #99

'''
<< 좌측시프트 
    원래값 * 2 ** bit수
>> 우측시프트
    원래값 / 2 ** 비트수
'''
print("=========<<")
x=8
y= x << 3
print(y)
print(8*2**3)

print("=========>>")
x=8
y= x >> 2
print(y)
print(8/2**2)


