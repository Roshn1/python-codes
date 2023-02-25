'''Program to find the Compound Interest compounded annually and the total amount when the
Principal, Rate of Interest and Time are entered by the user'''

p = int(input("Enter the principal amount"))
r = int(input("Enter the rate of interest "))
n = int(input("Enter the no. of times the interest is taken"))
t = int(input("Enter the time period"))

ci = p*(1+(r/n)**n*t)-p
print("COMPOUND INTEREST%.2f" % ci)
amt = ci+p
print("TOTOAL AMOUNT %.2f" % amt)