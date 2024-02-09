#basic shelve program to shelve a list

import shelve
num=[1,2,3,4,5]
with shelve.open("aaaa") as x:
    x["num"]=num
    print(x["num"])
    x["num"]=[11,22,33,44,55]
    x.sync()
    print(x["num"])