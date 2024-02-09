# to check if an element is available in the tuple / not

a=(1,2,3,4,5)
result=0
n=int(input("Enter the key:"))
for i in a:
    if n==i:
        result=1
        
if result==1:
    print("Present")
else:
    print("Not Present")