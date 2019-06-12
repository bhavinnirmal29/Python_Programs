num = int(input("Enter a number = "))
for i in range(2,num,1) :
    if(num%i==0) :
        flag = 0
    else :
        flag = 1
if(flag==0) :
    print("The number is prime")
else :
    print("The number is not prime")
