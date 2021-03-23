from tkinter import *
import json
import sc2TEST

ui=sc2TEST

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
    ui.list1.delete(0, END)
    statTXT=("Health: %s Attack: %s Speed: %s" % (hp, atk, sp))
    ui.list1.insert(END,statTXT)

def search(num):
    for item in roomJsn["room"+str(num)]:
        text1.insert(END, item + "\n")

def simpleLogic(query):
    if query == "look":
        return search(roomNum)

def cmd_function():
    print(cmdIN)
    simpleLogic(ui.cmd_txt.get())
    statChange()

def txtInsert(num):
    for item in messageJsn["msg"+str(num)]:
        print(item)
        ui.text1.insert(END, item + '\n' )



