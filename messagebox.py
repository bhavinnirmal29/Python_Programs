import tkinter
from tkinter import *
from tkinter import tkmessagebox

top = tkinter.Tk()
def hello():
   tkmessagebox.showinfo("Say Hello", "Hello World")

B1 = tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
