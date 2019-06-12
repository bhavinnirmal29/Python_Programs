import tkinter
from tkinter import*

top = tkinter.Tk()
c = tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = c.create_arc(coord, start=100, extent=350, fill="red")

c.pack()
top.mainloop()
