from tkinter import StringVar
import customtkinter
import globalVars
from threading import Thread
import Services.TelemetryService as TelemetryService

def Race_Director(self, parent_frame):

    self.frame_5 = customtkinter.CTkFrame(parent_frame,width=500)
    self.frame_5.grid(row=0,column=1,padx=20,pady=20,sticky='news')


    self.label = customtkinter.CTkLabel(self.frame_5,text='Race Director',width=800)
    self.label.grid(row=1, column=0,padx=10,pady=10)

    self.label2 = customtkinter.CTkLabel(self.frame_5,textvariable=globalVars.activated_StringVar,width=800)
    self.label2.grid(row=2, column=0,padx=10,pady=10)

    self.activate = customtkinter.CTkButton(self.frame_5,text='toggle connection',height=30,width=90,command=lambda: Handle_Toggle_Connection(self))
    self.activate.grid(row=2, column=1,padx=10,pady=10)

    def Handle_Toggle_Connection(self):        
        globalVars.set_activated()
