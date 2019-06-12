from tkinter import *
def add_():
    a_=E1.get()
    a = int(a_)
    b_=E2.get()
    b = int(b_)
    print("Addition = %d"%(a+b))

def sub():
    a_=E1.get()
    a = int(a_)
    b_=E2.get()
    b = int(b_)
    print("Subtraction = %d"%(a-b))

def mul():
    a_=E1.get()
    a = int(a_)
    b_=E2.get()
    b = int(b_)
    print("Multiplication = %d"%(a*b))

def div():
    a_=E1.get()
    a = int(a_)
    b_=E2.get()
    b = int(b_)
    print("Division = %d"%(a/b))

def modulo():
    a_=E1.get()
    a = int(a_)
    b_=E2.get()
    b = int(b_)
    print("Modulo = %d"%(a%b))
top = Tk()
top.geometry("200x400")
L1 = Label(top, text="Num 1 ")
L1.pack()
E1 = Entry(top, bd =4)
E1.pack()
L2 = Label(top,text="Num 2 ")
L2.pack()
E2 = Entry(top,bd = 4)
E2.pack()
b = Button(top,text="Add",width=20,command=add_)
b.pack(pady=10)
b1 = Button(top,text="Subtract",width=20,command=sub)
b1.pack(pady=10)
b2 = Button(top,text="Multiply",width=20,command=mul)
b2.pack(pady=10)
b3 = Button(top,text="Division",width=20,command=div)
b3.pack(pady=10)
b4=Button(top,text="Modulo",width=20,command=modulo)
b4.pack(pady=10)

top.mainloop()
