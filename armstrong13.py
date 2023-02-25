''' Program to check the given number is armstrong numbers or not'''

n = int(input("Enter a number"))
s = n
b = len(str(n))
sum1 = 0 
while n!=0 :
    r = n % 10
    sum1 = sum1 + r ** b
    n = n//10

if s == sum1 :
    print("Armstrong number")

else :
    print("Not an armstrong number")