from tkinter import *
import json
import script1
import script2
from script3 import Database

database=Database()

def insert_command():
    database.insert("Cup", 6)

window = Tk()
window.wm_title("BUTTON WINDOW")

b1=Button(window,text="Insert random",command=insert_command)
b1.grid(row=0,column=0)


window.mainloop()