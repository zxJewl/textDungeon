from tkinter import *
import json
import script1

bgc=script1

global cmd_txt

##!!! MAIN WINDOW !!!##
window = Tk()
window.wm_title("Text Dungeon")

##!! LABELS !!##

l1=Label(window,text="Stats:")
l1.grid(row=0,column=0)

l2=Label(window,text="")
l2.grid(row=1,column=1)

l3=Label(window,text="",width=5)
l3.grid(row=1,column=200)
##!! ENTRIES !!##

global cmd_txt
cmd_txt=StringVar()
e1=Entry(window,textvariable=cmd_txt,width=100)
e1.grid(row=2,column=1,columnspan=100)

##!! LISTS !!##
#> Stat Box
list1=Listbox(window,height=1,width=40)
list1.grid(row=0,column=1,columnspan=4)
bgc.statChange()
#<

#> Main Text Window
text1=Text(window,width=90, height=20)
text1.grid(row=1,column=1,columnspan=190)
text1.bind("<Key>", lambda e: "break")

bgc.txtInsert("Start")
#<

##!! BUTTONS !!##

b1=Button(window,text="Command:",command=bgc.cmd_function)
b1.grid(row=2,column=0)



pholder1=Button(window,text="Change HP", width=12,command=bgc.hp_change)
pholder1.grid(row=3,column=1)

pholder2=Button(window,text="Show HP", width=12,command=bgc.hp_show)
pholder2.grid(row=3,column=2)



window.mainloop()
