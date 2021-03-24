from tkinter import *
import json
import script1
import script2
from script3 import Database
bgc = script1


database=Database()

def viewINV():
    invList.delete(0,END)
    for row in database.view():
        invList.insert(END,row[1:])

def insert_command():
    database.insert("Cup", 6)
    viewINV()

def placeItemDel():
    database.delete(selected_tuple[0])
    viewINV()
    
def get_selected_row(event):
    try:
        global selected_tuple
        index=invList.curselection()[0]
        selected_tuple=invList.get(index)
        e1.delete(0,END)
        e1.insert(END, selected_tuple[0])
    except IndexError:
        pass

window = Tk()
window.wm_title("BUTTON WINDOW")

b1=Button(window,text="Insert random",command=insert_command)
b1.grid(row=0,column=0)

b2=Button(window,text="Delete",width=12,command=placeItemDel)
b2.grid(row=1,column=0)

placeholdItem=StringVar()
e1=Entry(window,textvariable=placeholdItem,width=20)
e1.grid(row=1,column=2)


invList=Listbox(window,height=10,width=100)
invList.grid(row=7,column=1,columnspan=100)
viewINV()
invList.bind('<<ListboxSelect>>', get_selected_row)

sb1=Scrollbar(window)
sb1.grid(row=7,column=101,rowspan=6)

invList.configure(yscrollcommand=sb1.set)
sb1.configure(command=invList.yview)

window.mainloop()