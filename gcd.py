#gcd using euclid's method

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
x=int(input("Enter the first value:"))
y=int(input("Enter the second value:"))
print(gcd(x,y))  
