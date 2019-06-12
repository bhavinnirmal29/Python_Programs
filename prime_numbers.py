#Range Of Prime Numbers
start = int(input("Enter start range  : "))
end = int(input("Enter end range : "))
for i in range(start,end,1):
    for j in range(2,start,1) :
        if(start%j!=0):
            flag=0
        else:
            flag=1

    if(flag==0):
        print(start)
