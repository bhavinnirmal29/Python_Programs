import tkinter
from tkinter import *
def getValues(e):
    s = e.get()
    ans = int(s)
t=1
def fact():
    if(ans==1):
        return 0
    else:
        t = ans*fact(n-1)
        return t
def show():
    fact()
    print(fact(ans))
root=Tk()
l1 = Label(root,text="Num 1 : ")
l1.pack(side=LEFT)
e1=Entry(root,width=30)
e1.pack(side=LEFT)
getValues(e1)
button = Button(root,text="Factorial",width=25,command=show)
button.pack()
root.mainloop()
