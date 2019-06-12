from tkinter import *

counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
 
root = Tk()
root.title("Counting Seconds")
root.geometry("200x100")
label = Label(root, fg="green",font="Times 20 italic")
label.pack()
counter_label(label)
button = Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()
