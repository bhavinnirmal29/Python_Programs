from tkinter import *
master = Tk()
whatever_you_do = "Whatever you do will be insignificant,but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
master.geometry("1000x300")
l = Label(master,text=whatever_you_do)
l.config(bg='blue', font=('times', 24, 'italic'))
l.pack()
msg.pack(pady=10)
master.mainloop( )
