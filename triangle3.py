a = int(input("enter the first side"))
b = int(input("enter the second side"))
c = int(input("enter the third side"))
if (a==b and  b == c and c==a):
    print("triangle is an equilateral triangle")

elif(a!=b and b!=c and c!=a):
    print("triangle is a scalene triangle") 

else :
    print("triangle is an isosceles triangle")      