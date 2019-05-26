import time
import sys

sys.path.append("e:/study/python/dev01_vscode/module")
import mod1





def salePrice(price) :
     return price - price *0.1
    

price = salePrice(1000)
print(price , time.asctime())
print(time.clock())
