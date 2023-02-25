'''Program to find the sum of digits of an entered number.'''

num = int(input("Enter the number"))
ssum = 0
nnum = num
while(nnum!=0):
    digit = nnum % 10
    nnum = nnum // 10
    ssum = ssum + digit
print("SUM =", ssum)