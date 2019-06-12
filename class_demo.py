class Student:
    "Student Marks"
    def getData(a,b,c):
        total=a+b+c
        print("Maths - ",a)
        print("English - ",b)
        print("Science - ",c)
        avg=total/3
        print("Average Marks = ",avg)
        if(a>b and a>c):
            print("Maths Marks is Greatest")
        elif(b>a and b>c):
            print("English Marks is Greatest")
        elif(c>a and c>b):
            print("Science Marks is Greatest")

s1=int(input("Enter Marks for Maths = "))
s2=int(input("Enter Marks for English = "))
s3=int(input("Enter Marks for Science = "))
ob = Student
ob.getData(s1,s2,s3)
