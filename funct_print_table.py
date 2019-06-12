num=int(input("Enter a number = "))
i=1

def print_Table(num,j):
    return(num*j)
while i <=10 :
    ans=print_Table(num,i)
    print("%d x %d = %d"%(num,i,ans))
    i=i+1
    
