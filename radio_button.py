from tkinter import *

root = Tk()

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

lang = [
    ("HTML",6),
    ("AJAX",7),
    ("JSON",8),
    ("R",9)
    ]

def ShowChoice():
    print( v.get())

Label(root, 
      text="Choose your favourite programming language:",
      justify = LEFT,
      padx = 20).pack()

for txt, val in languages:
    Radiobutton(root, 
                text=txt,
                padx = 20, 
                variable=v, 
                command=ShowChoice,
                value=val).pack(anchor=W)

Label(root,text="Choose Language",justify=LEFT,padx=20).pack()

for txt,val in lang:
    Radiobutton(root,text=txt,padx=20,variable=v,command=ShowChoice,value=val).pack(anchor=W)
    
mainloop()







