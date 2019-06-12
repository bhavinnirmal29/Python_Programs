s1=int(input("Enter marks of Maths out of 100\n"))
s2=int(input("Enter marks of Science out of 100\n"))
s3=int(input("Enter marks for English out of 100\n"))
total = s1+s2+s3
print("Total Marks out of 300 = %d"%(total))
per=float((s1+s2+s3)*100/300)
print("Percentage = %f"%(per))
if per>=60 :
    print("Grade A")
elif per>=50 and per<=60:
    print("Grade B")
elif per>=40 and per<50:
    print("Grade C")
else:
    print("Fail")
