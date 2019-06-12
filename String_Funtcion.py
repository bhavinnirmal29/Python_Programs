print("count()-------------------------")
msg = "welcome to sssit";  
substr1 = "o";  
print(msg.count(substr1, 4, 16))
substr2 = "t";  
print(msg.count(substr2))

print("endswith()-----------------------")
string1="Welcome to SSSIT";  
substring1="SSSIT";  
substring2="to";  
substring3="of";  
print (string1.endswith(substring1))
print (string1.endswith(substring2,2,16))  
print (string1.endswith(substring3,2,19))
print (string1.endswith(substring3))

print("find()----------------------------")
str="Welcome to SSSIT";  
substr1="come";  
substr2="to";  
print (str.find(substr1))
print (str.find(substr2)) 
print (str.find(substr1,3,10))
print (str.find(substr2,5))

print("index()---------------------------")
str="Welcome to world of SSSIT";  
substr1="come";  
substr2="of";  
print (str.index(substr1))
print (str.index(substr2))
print (str.index(substr1,3,10)) 
print (str.index(substr2,17))

print("isalnum()---------------------------")
str="Welcome to sssit";  
print(str.isalnum())
str1="Python47";  
print (str1.isalnum())

print("isalpha()-----------------------------")
string1="HelloPython";    # Even space is not allowed  
print (string1.isalpha())
string2="This is Python2.7.4"
print (string2.isalpha())

print("isdigits()------------------------------")
string1="HelloPython";   
print (string1.isdigit())
string2="98564738"
print (string2.isdigit())

print("islower()---------------------------------")
string1="Hello Python";   
print(string1.islower())
string2="welcome to "  
print(string2.islower())

print("isupper()-----------------------------------")
string1="Hello Python";   
print (string1.isupper())
string2="WELCOME TO"  
print (string2.isupper())

print("isspace()----------------------------------")
string1="    ";   
print (string1.isspace())
string2="WELCOME TO WORLD OF PYT"  
print (string2.isspace())

print("len()--------------------------------------")
string1="    ";   
print (len(string1))
string2="WELCOME TO SSSIT"  
print (len(string2))

print("lower()--------------------------------------")
string1="Hello Python";   
print (string1.lower()) 
string2="WELCOME TO SSSIT"  
print(string2.lower())

print("upper()---------------------------------------")
string1="Hello Python";   
print (string1.upper()) 
string2="welcome to SSSIT"  
print (string2.upper())

print("startswith()-----------------------------------")
string1="Hello Python";   
print(string1.startswith('Hello'))
string2="welcome to SSSIT"
print(string2.startswith('come',3,7))

print("swapcase()--------------------------------------")
string1="Hello Python";   
print(string1.swapcase())
string2="welcome to SSSIT"  
print(string2.swapcase())

print("istrip()-----------------------------------------")
string1="    Hello Python"
print(string1.lstrip())
string2="@@@@@@@@welcome to SSSIT"
print(string2.lstrip('@'))

print("rstrip()---------------------------------------")
string1="    Hello Python     ";   
print(string1.rstrip())
string2="@welcome to SSSIT!!!"
print (string2.lstrip('@'))
