myList=[]
ch=0
print("Empty List = ",myList)
n=int(input("Enter number of elements you want to enter "))
for i in range(0,n) :
    num = int(input("Enter Element = "))
    myList.insert(i,num)
    print("MyList = ",myList)
while ch!=6 :
    print("1-Append\n2-Insert\n3-Remove\n4-Pop\n5-Clear\n6-Exit\n7-Display")
    ch=int(input("Enter your choice = "))
    if ch==1:
        num1=int(input("Enter number : "))
        myList.append(num1)
    elif ch==2:
        num1=int(input("Enter number : "))
        myList.insert(len(myList),num1)
    elif ch==3:
        num1=int(input("Enter index : "))
        myList.remove(num1)
    elif ch==4:
        num1=int(input("Enter index : "))
        myList.pop(num1)
    elif ch==5:
        myList.clear()
        print("MyList = ",myList)    
    elif ch==6:
        break
    elif ch==7:
        print("MyList = ",myList)
