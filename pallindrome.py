num=int(input("Enter a number "))
temp=num
#num1 = 0
rev=0
new_num = 0
while num!=0 :
    rem=int(num%10)
    rev=int(rev*10+rem)
    num=int(num/10)
print(rev)
if(rev==temp):
    print("The number is pallindrome")
else:
    print("The number is not pallindrome")

    
