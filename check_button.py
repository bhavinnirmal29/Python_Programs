from tkinter import *

root = Tk()

Label(root,text="Choose programming Language : ").pack()

def show():
    print("python {}, java {}, C {}, C++ {}".format(p.get(),j.get(),c.get(),cpp.get()))



p = IntVar()
j = IntVar()
c = IntVar()
cpp = IntVar()
Checkbutton(root,text="Python",variable=p).pack()
Checkbutton(root,text="java",variable=j).pack()
Checkbutton(root,text="C",variable=c).pack()
Checkbutton(root,text="C++",variable=cpp).pack()

Button(root,text="show",command=show).pack()
Button(root,text="Quit",command=root.destroy).pack()


root.mainloop()
