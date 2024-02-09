# celsius to fahrenheit / vice versa

ch=int(input("Enter your choice\n1.Celsius\n2.Fahrenheit\n"))

if ch==1:
    c=float(input("Enter temperature in Celsius:"))
    f=(c*9/5)+32
    print(c," degree Celsius is equal to ",f," degree Fahrenheit")

elif ch==2:
    f=float(input("Enter temperature in Fahrenheit:"))
    c=(f-32)*5/9
    print(f," degree Fahrenheit is equal to ",c," degree Celsius")