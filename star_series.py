num=int(input("Enter a number = "))
string = ""
for i in range(0,num+1,1):
    for j in range(0,i,1):
        string = string + "*"

    print(string)
    string=""
    

    
