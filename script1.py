from tkinter import *
import json
import script2
import sqlite3
from script3 import Database

invData=Database()
ui=script2

# player stats
hp = 20
st = 0
sp = 5
df = 0.05
atk = 5

#enemey stat variables
global Ehp
global Eatk
global Esp
global Edef
Ehp  = 1
Eatk = 0
Esp  = 0
Edef = 0

global enemy
enemy = "slime"
global roomNum
roomNum=0
global engaged 
engaged = False

global roomJsn
roomJsn = json.load(open("files/Rooms.json"))

global messageJsn
messageJsn = json.load(open("files/messages.json"))

global opponent
opponent = json.load(open("files/enemies.json"))

#<< PLACE HOLDER CMDS >>#
def hp_change():
    global hp
    hp=hp+1
    print(hp)
    statChange()
def hp_show():
    print(hp)
#<<END>>#

def statChange():
    ui.list1.delete(0, END)
    statTXT=("Health: %s Attack: %s Speed: %s" % (hp, atk, sp))
    ui.list1.insert(END,statTXT)

def enemyStat():
    ui.eList.delete(0, END)
    EstatTXT=("Health: %s Attack: %s Speed: %s" % (Ehp, Eatk, Esp))
    if engaged == False:
        ui.eList.delete(0,END)
        ui.eList.insert(END, "You are curently unengaged")
    elif engaged == True:
        ui.eList.delete(0,END)
        ui.eList.insert(END, EstatTXT)
        print("Elist has engaged")
    else:
        ui.eList.insert("EROOR")

def viewINV():
    ui.invList.delete(0,END)
    for row in invData.view():
        ui.invList.insert(END,row[1:])

#<< USER HELP DEFS >>
def hep():
    with open("files/help.txt") as helpFile:
        helpTXT = helpFile.read()
    ui.text1.insert(END, helpTXT)

def actions(num):
    for item in roomJsn["cmdRoom"+str(num)]:
        ui.text1.insert(END, item+'\n')
        ui.text1.see(END)

def insertUI(info):
    ui.text1.insert(END, info)
    ui.text1.see(END)

def door1():
    global roomNum
    while True:
        if roomNum == 1:
            print("")
            ui.text1.insert(END, "   You walk back into the room you woke in.")
            print("")
            roomNum = 0
            search(roomNum)
            ui.e1.delete(0, END)
            break    
        if roomNum == 0:
            print("")
            ui.text1.insert(END,"   You push open the door.")
            roomNum = 1
            search(roomNum)
            ui.e1.delete(0, END)
            break

def drops(e):
    for item in opponent[e+"Drop"]:
        ui.text1.insert(END, item + "\n")



def search(num):
    for item in roomJsn["room"+str(num)]:
        ui.text1.insert(END, item + "\n")

def simpleLogic(query):
    if query == "look":
        return search(roomNum)
        
    if query == "help":
        hep()

    if query == "actions":
        actions(roomNum)
    
    enemyStat()
    

def roomLogic(query):
    if query == "delete":
        ui.eList.delete(0,END)
        print("BUG01")
    global roomNum
    if roomNum == 0:
        if query == "go through the wooden door":
            door1()  
            query=""

    if roomNum == 1:
        if query == "go through the wooden door":
            door1()
            query=""    
        if query == "go right": 
            insertUI("   You go into the room marked 'DANGER'")
            roomNum=2
            search(roomNum)
    
    #room 2 logic
    if roomNum == 2:

        if query == "leave the room":
            print("")
            insertUI("    You exit the DANGEROUS room, thankfull to have leave it behind.")
            print("")
            roomNum = 1
            search(roomNum)  

        if query == "fight the slime":
            global engaged
            engaged=True
            enemyStat()
            #fight()
            print("ENGAGED")


def cmd_function():
    print(ui.cmd_txt.get().lower())
    simpleLogic(ui.cmd_txt.get().lower())
    roomLogic(ui.cmd_txt.get().lower())
    statChange()
    ui.text1.see(END)
    ui.e1.delete(0, END)

def msgInsert(num):
    for item in messageJsn["msg"+str(num)]:
        print(item)
        ui.text1.insert(END, item + '\n' )



