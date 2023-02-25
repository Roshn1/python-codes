


count = 0
num = int(input("enter the number"))
for i in range(1,num+1):
    if(num%i==0):
        count +=1
if(count==2):
        print("PRIME NUMBER")

else:
    print("NOT A PRIME NUMBER")