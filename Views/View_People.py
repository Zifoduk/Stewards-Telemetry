import tkinter
import tkinter.messagebox
import customtkinter
import os
from PIL import Image, ImageTk
from settings import GetImageFilePath

def People(self, parent_frame):        
    self.frame_4 = customtkinter.CTkFrame(parent_frame,width=800)
    self.frame_4.grid(row=0,column=1,padx=20,pady=20,sticky='news')

    self.label = customtkinter.CTkLabel(self.frame_4,text='Player Data',width=800)
    self.label.grid(row=1, column=0,padx=10,pady=10)