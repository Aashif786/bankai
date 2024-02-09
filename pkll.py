#pickling a file 

import pickle
file="f3.txt"
a=["hiiiii ","helloo"]
with open(file,"wb") as x:
    pickle.dump(a,x)
with open (file,"rb") as y:
    print(pickle.load(y))