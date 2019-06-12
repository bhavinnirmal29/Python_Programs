start=int(input("Enter Start Range = "))
end=int(input("Enter End Range = "))
flag=0
for num in range(start,end+1):
    for j in range(2,num):
        if(num%j==0):
            flag=0
            break
        else:
            flag=1

    if(flag==1):
        print(num)
