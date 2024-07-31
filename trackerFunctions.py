import tkinter as tk
import json
import os
from tkinter import messagebox
from threading import Timer

#import json file and return the data in readable format
def getJsonData(configpath):
    if os.path.isfile(configpath):
            with open(configpath) as rawJson:
                jsondata = json.load(rawJson)
                return jsondata
    else:
        return "error - no data found"

    #get bossdata out of a json structure
def getBossData(jsondata):
    for key, value in jsondata.items():
        if key == "bosses" :
            bossvalues = value
    return bossvalues

#def writeInfo(eventObject,returnvalue):
#    print(returnvalue)


def popupbosstimer(map, boss, respawn, timeformat):
    if timeformat == "m":
        countertime = respawn * 60
    elif timeformat == "h":
        countertime = respawn * 60
    elif timeformat == "s":
        countertime = respawn * 1
    else:
        messagebox.showwarning("Warning", "timeformat not correct. Please only use 'm', 'h', 's'")
        return

    messagebox.showinfo("Information", "Timer for Boss "+boss+" in map "+map+" startet")
    bosstimer = Timer(countertime, boss_spawned, a)
    

def boss_spawned(map, boss):
    messagebox.showinfo("Information", boss+" at "+map+" respawning soon")
    return