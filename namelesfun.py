add = lambda a,b:a+b
sub = lambda a,b:a-b
mul = lambda a,b:a*b
div = lambda a,b:a/b
mod = lambda a,b:a%b
print("1-Add\n2-Sub\n3-Mul\n4-Div\n5-Mod\n6-Exit")
ch = int(input("Enter your choice : "))
a=int(input("Enter a number = "))
b=int(input("Enter a number = "))
while ch!=6 :
    if(ch==1):
        print("Add = ",add(a,b))
    elif (ch==2):
        print("Sub = ",sub(a,b))
    elif (ch==3):
        print("Mul = ",mul(a,b))
    elif (ch==4):
        print("Div = ",div(a,b))
    elif (ch==5):
        print("Mod = ",mod(a,b))
    elif (ch==6):
        break
    else:
        print("Invalid Choice ")
        break
    ch=int(input("Enter your choice : "))
    if ch!=6:
        a=int(input("Enter a number = "))
        b=int(input("Enter a number = "))
