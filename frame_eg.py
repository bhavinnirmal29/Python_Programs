from tkinter import *

class App:

    def __init__(self,master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT,padx=10)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT,padx=10)

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()
root.geometry("300x300")
root.resizable(0,0)
app = App(root)
root.mainloop()
root.destroy()
