'''Program to find the factorial of an entered number'''

num = int(input("Enter the number"))
fac =1
a = 1
while a<=num:
    fac = fac * a
    a+=1
    
print("FACTORIAL OF A NUMBER = ", fac)