from tkinter import *
import json
import script2

# player stats
hp = 20
st = 0
sp = 5
df = 0.05
atk = 5

roomNum=0

global roomJsn
roomJsn = json.load(open("files/Rooms.json"))

global messageJsn
messageJsn = json.load(open("files/messages.json"))

##!! definitions !!##

def hp_change():
    global hp
    hp=10
    print(hp)
    statChange()
def hp_show():
    print(hp)

def statChange():
    list1.delete(0, END)
    statTXT=("Health: %s Attack: %s Speed: %s" % (hp, atk, sp))
    list1.insert(END,statTXT)

def cmd_function():
    print(cmd_txt.get().lower())
    script2.runLogic1(cmd_txt.get().lower())
    list2.insert(END, script2.search())

def txtInsert(num):
    for item in messageJsn["msg"+str(num)]:
        print(item)
        list2.insert(END, item)



##!!! MAIN WINDOW !!!##
window = Tk()
window.wm_title("Text Dungeon")

##!! LABELS !!##

l1=Label(window,text="Stats:")
l1.grid(row=0,column=0)

l2=Label(window,text="")
l2.grid(row=1,column=1)

##!! ENTRIES !!##

cmd_txt=StringVar()
e1=Entry(window,textvariable=cmd_txt,width=100)
e1.grid(row=2,column=1,columnspan=100)

##!! LISTS !!##
#> Stat Box
list1=Listbox(window,height=1,width=40)
list1.grid(row=0,column=1,columnspan=4)
statChange()
#<

#> Main Text Window
list2=Listbox(window,width=100, height=20)
list2.grid(row=1,column=1,columnspan=100)

sb1=Scrollbar(window)
sb1.grid(row=1,column=101,rowspan=10)

list2.configure(yscrollcommand=sb1.set)
sb1.configure(command=list2.yview)

txtInsert("Start")
#<

##!! BUTTONS !!##

b1=Button(window,text="Command:",command=cmd_function)
b1.grid(row=2,column=0)

pholder1=Button(window,text="Change HP", width=12,command=hp_change)
pholder1.grid(row=3,column=1)

pholder2=Button(window,text="Show HP", width=12,command=hp_show)
pholder2.grid(row=3,column=2)



window.mainloop()
