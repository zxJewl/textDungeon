import json
from tkinter import *

# player stats
hp = 20
st = 0
sp = 5
df = 0.05
atk = 5

#slime stats
slhp = 15
slatk = 1
slsp = 2
sldf = 0

gameStop = False
note1 = True
engaged = False
global ent1
ent1 = False
global enemy
enemy = "slime"

global hl1
global hl2
hl1 = False
hl2 = False

global inv 
inv = [""]

global roomJsn
roomJsn = json.load(open("files/Rooms.json"))

global opponent
opponent = json.load(open("files/enemies.json"))

global items
items = json.load(open("files/items.json"))


global roomNum
roomNum = 0

global test
test = True

def insert(txt):
    list2.insert(txt)

def search(num):
    for item in roomJsn["room"+str(num)]:
        srchOUT=item

def runLogic1(cmd):
    if cmd == "look":
        print("Command = look")
        search(roomNum)
        print(search(roomNum))
        return search(roomNum)
        
        
