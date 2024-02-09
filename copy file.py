# copy contents of a file to another

with open("f1.,txt","r") as x:
    q=x.read()
with open("f2.txt","w") as y:
    y.write(q)
print("File f1 has been copied to file f2.")








