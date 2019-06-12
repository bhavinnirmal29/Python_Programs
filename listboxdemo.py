from tkinter import *
import tkinter as tk
top = tk.Tk()
Lb1 = tk.Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.grid(row=0,column=1)
top.geometry("300x300")
top.mainloop()
