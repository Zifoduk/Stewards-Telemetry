from tkinter import *

#activated = "False"
activated_StringVar = None
activated = False

app_Open = True

def initialize():
    global activated_StringVar, activated
    activated_StringVar = StringVar()
    print ("initalized")
    set_activated()

def set_activated():
    global activated_StringVar, activated
    if(activated_StringVar.get() == "Offline"):
        activated_StringVar.set("Online")
        activated = True
    else:
        activated_StringVar.set("Offline")
        activated = False