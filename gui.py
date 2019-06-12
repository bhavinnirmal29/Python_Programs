import tkinter
from tkinter import *

explanation="Hello World"
top = tkinter.Tk()
top.title("Demo example")
top.geometry("500x500")
top.resizable(0,0)
top.wm_iconbitmap("Mario.ico")
l1 = Label(top,text="Number 1 = ")
l2 = Label(top,text="Number 2 = ")
l3 = Label(top,text="Answer = ")
pi=PhotoImage(file="cartoon.gif")
l0=Label(top,image=pi,text=explanation,compound=CENTER)
l0.config(font=('Times',22,'bold'))
l0.pack(side="bottom")
l1.config(fg="blue",bg="black",font=('Times',24,'normal'))
l1.pack(pady=10)
l2.config(font=('Times',24,'normal'))
l2.pack(pady=10)
l3.config(font=('Times',24,'normal'))
l3.pack(pady=10)
# Code to add widgets will go here...
top.mainloop()

