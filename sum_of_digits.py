num=int(input("Enter a number "))
sum1 = 0
num1 = 3
while (num1!=0) :
    num1 = int(num%10)
    num = int(num/10)
    sum1=sum1+num1
print(sum1)
