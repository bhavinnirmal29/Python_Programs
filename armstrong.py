num=int(input("Enter a number "))
temp=num
sum1 = 0
num1 = 1
while (num1!=0) :
    num1 = int(num%10)
    num = int(num/10)
    sum1=sum1+(num1*num1*num1)
if(sum1==temp):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
