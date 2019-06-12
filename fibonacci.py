x=0
y=1
sum1=0
i=0
num = int(input("Enter End Range = "))
for i in range(1,num,1):
    sum1=x+y
    x=y
    y=sum1
    print("%d"%(sum1))
