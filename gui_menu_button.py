from tkinter import*

top = Tk()

mb=  Menubutton ( top, text="condiments", relief=RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
v  = IntVar()
v1 = IntVar()
def show_choice(v2):
    print(v2)

mb.menu.add_checkbutton ( label="mayo",
                          variable=v,command=show_choice("mayo"))
mb.menu.add_checkbutton ( label="ketchup",
                          variable=v1,command=show_choice("ketchup"))

mb.pack()
top.mainloop()
