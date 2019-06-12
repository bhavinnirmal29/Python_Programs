num=int(input("Enter a number = "))
string = ""
for i in range(num,0,-1):
    for j in range(i,0,-1):
        string = string + "*"

    print(string)
    string=""
    

    
