'''Program to find the Simple Interest and the total amount when the Principal, Rate of Interest
and Time are entered by the user.
'''

p = int(input("Enter the Principal amount"))
r = int(input("Enter the rate of interest"))
t = int(input("Enter the time"))

si = (p*r*t)/100
print("Simple interest amount = ",si)
amt = p*(1+r*t)
print("Total Amount = ",amt)