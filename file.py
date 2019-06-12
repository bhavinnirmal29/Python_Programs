#f = open("test3.txt","r")
#print(f.read())                                     # Reading From A File
with open("test3.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
   print("Written Successfully")
  
f = open("test3.txt","r",encoding = 'utf-8')
print(f.read(15))

