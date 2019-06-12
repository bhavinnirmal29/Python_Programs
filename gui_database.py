from tkinter import *
import sqlite3

def show_entry_fields():
   conn = sqlite3.connect("C:\Python36-32\sqlite3/raj.db")
   cursor = conn.cursor()
   results = cursor.fetchall()
   for row in results:
      print("First Name: %s\nLast Name: %s" % (row[0],row[0]))


def insert_data():
    fn = e1.get()
    ln = e2.get()
    conn = sqlite3.connect("C:\Python36-32\sqlite3/raj.db")
    cursor = conn.cursor()
    cursor.execute("insert into infodb values('%s','%s')"%(fn,ln))
    conn.commit()
    conn.close()
    print("Data Inserted")
'''
def delete_data():
    def deletion():
        conn1 = sqlite3.connect("C:\Python36-32\sqlite3/raj.db")
        cursor1 = conn1.cursor()
        cursor1.execute("delete from infodb where name = "%(i))
        conn1.commit()
        conn1.close()
    root=Tk()
    Label(root,text="Enter name").grid(row=0)
    e3 = Entry(root)
    e3.grid(row=0,column=1)
    i = e3.get()
    Button(root,text='Enter',command = deletion).grid(row=1,column=0,sticky =E,pady=14)
    
    def deletion():
        conn1 = sqlite3.connect("C:\Python36-32\sqlite3/raj.db")
        cursor1 = conn1.cursor()
        cursor1.executeQuery("delete from infodb where first_name = "%(i))
        conn1.commit()
        conn1.close()
'''
master = Tk()

Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.destroy).grid(row=3, column=0, sticky=E, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=14)
Button(master, text='Insert', command=insert_data).grid(row=3,column=1,sticky=E, pady=4)
#Button(master, text='Delete', command=delete_data).grid(row=3,column=1,sticky=W,pady=4)
mainloop()
