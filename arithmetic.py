n1=int(input("Enter num1 \n"))
n2=int(input("Enter num2 \n"))
print("Enter your choice : \n1 - Addition \n2 - Subtraction \n3 - Multiplication\n4 - Division \n5 - Modulo\n")
choice = int(input("Enter your choice \n"))
if(choice == 1) :
    print("Addition = ",(n1+n2))
elif(choice ==2) :
    print("Subtraction = ",(n1-n2))
elif(choice ==3) :
    print("Multiplication = ",(n1*n2))
elif(choice ==4) :
    print("Division = ",(n1/n2))
elif(choice ==5) :
    print("Modulo = ",(n1%n2))
else :
    print("Invalid Choice ")
    
