import tkinter
from tkinter import ttk,filedialog
import tkinter.messagebox
import customtkinter
import os
from PIL import Image, ImageTk
from settings import *
from Utilities import Util_ViewThemes as UVT
import json
from app import Theme_Dict
import Views.View_Settings



def People(self, parent_frame):        
    self.frame_4 = customtkinter.CTkFrame(parent_frame,width=800)
    self.frame_4.grid(row=0,column=1,padx=20,pady=20,sticky='news')

    self.label = customtkinter.CTkLabel(self.frame_4,text='Player Data',width=800)
    self.label.grid(row=1, column=0,padx=10,pady=10)


    frame_1 = customtkinter.CTkFrame(master=parent_frame)

    frame_1.grid(row=1,column=1,padx=20,pady=0,sticky='news')
   

    treestyle = ttk.Style()
    treestyle.theme_use('default')
    treestyle.configure("Treeview", 
                        background=Theme_Dict['CTkFrame']['fg_color'][Views.View_Settings.Theme_Mode],
                        foreground=Theme_Dict['CTkLabel']['text_color'][Views.View_Settings.Theme_Mode],
                        fieldbackground=Theme_Dict['CTkFrame']['top_fg_color'][Views.View_Settings.Theme_Mode],
                        borderwidth=0,
                        rowheight=30
                        )

    treestyle.map('Treeview', background=[('selected', Theme_Dict['CTkFrame']['fg_color'][Views.View_Settings.Theme_Mode])],
                        foreground=[('selected', Theme_Dict['CTkButton']['fg_color'][Views.View_Settings.Theme_Mode])])
    
    self.bind("<<TreeviewSelect>>", lambda event: self.focus_set())

    ##Treeview widget
    treeview = ttk.Treeview(frame_1, height=6, show="tree")
    treeview.grid(row=1,column=1,rowspan=10,padx=20,pady=20,ipadx=20,ipady=20)


    treeview.insert('', '0', 'i1', text ='Drivers')




    treeScroll = customtkinter.CTkScrollbar(
        frame_1,
        button_color=Theme_Dict['CTkFrame']['fg_color'][Views.View_Settings.Theme_Mode],
        button_hover_color=Theme_Dict['CTkButton']['fg_color'][Views.View_Settings.Theme_Mode]
        )

    treeScroll.configure(command=treeview.yview)
    treeview.configure(yscrollcommand=treeScroll.set)
    treeScroll.grid(row=1,column=2,pady=20,sticky='nws')


    
    def Driver_Import():

        filetypes = (
        ('All files', '*.*'), 
        ('text files', '*.txt')        
        )

        filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='D:\Files\GitHub\Stewards-Telemetry\Data',
        filetypes=filetypes)

        Driver_List = json.load(open(filename,encoding='UTF-8'))

        for i in Driver_List:
            treeview.insert('i1',customtkinter.END,i['Name'],text=i['Name'])
            if 'RealName' in i.keys():
                treeview.insert(i['Name'],customtkinter.END,text=i['RealName'])
            
            if 'Nationality' in i.keys():
                treeview.insert(i['Name'],customtkinter.END,text=i['Nationality'])
            
            if 'LeagueRole' in i.keys():
                treeview.insert(i['Name'],customtkinter.END,text=i['LeagueRole'])
            
            if 'RaceNumber' in i.keys():
                treeview.insert(i['Name'],customtkinter.END,text=i['RaceNumber'])


    

    def Driver_Enter():
        # dialog = customtkinter.CTkInputDialog(text='Type in a name:',title="New Driver")


        window = customtkinter.CTkToplevel()
        window.geometry("360x300")
        label = customtkinter.CTkLabel(window, text="Driver Details:")
        label.grid(row=0,column=0,columnspan=2, padx=40, pady=10)

        entry1 = customtkinter.CTkEntry(master=window,
                               placeholder_text="User Name",
                               width=320,
                               height=30,
                               border_width=2,
                               corner_radius=10)

        entry1.grid(row=1,column=0,columnspan=2,padx=10,pady=5)

        entry2 = customtkinter.CTkEntry(master=window,
                               placeholder_text="Real Name",
                               width=320,
                               height=30,
                               border_width=2,
                               corner_radius=10)

        entry2.grid(row=2,column=0,columnspan=2,padx=10,pady=5)

        entry3 = customtkinter.CTkEntry(master=window,
                               placeholder_text="Country",
                               width=320,
                               height=30,
                               border_width=2,
                               corner_radius=10)

        entry3.grid(row=3,column=0,columnspan=2,padx=10,pady=5)

        entry4 = customtkinter.CTkEntry(master=window,
                               placeholder_text="Role",
                               width=320,
                               height=30,
                               border_width=2,
                               corner_radius=10)

        entry4.grid(row=4,column=0,columnspan=2,padx=10,pady=5)

        entry5 = customtkinter.CTkEntry(master=window,
                               placeholder_text="Driver Number",
                               width=320,
                               height=30,
                               border_width=2,
                               corner_radius=10)

        entry5.grid(row=5,column=0,columnspan=2,padx=10,pady=5)

        def cancel():
            window.destroy()

        def Enter():

            Name = entry1.get()

            treeview.insert('i1',customtkinter.END,Name,text=Name)
            treeview.insert(Name,customtkinter.END,text=entry2.get())
            treeview.insert(Name,customtkinter.END,text=entry3.get())
            treeview.insert(Name,customtkinter.END,text=entry4.get())
            treeview.insert(Name,customtkinter.END,text=entry5.get())


            





            window.destroy()

        Cancel = customtkinter.CTkButton(window,
            text='Cancel',
            command=cancel
        )
        Cancel.grid(row=6,column=1,padx=20,pady=5,sticky='e')

        Enter = customtkinter.CTkButton(window,
            fg_color='#019000',
            text='Enter',
            command=Enter
        )
        Enter.grid(row=6,column=0,padx=20,pady=5,sticky='w')

        
        


    self.Driver_Entry = customtkinter.CTkButton(frame_1,
        text='Enter Driver Details',
        command=Driver_Enter
        )
    self.Driver_Import = customtkinter.CTkButton(frame_1,
        text='Import Drivers',
        command=Driver_Import
        )

    frame_1.grid_columnconfigure(3, minsize=100)
    self.Driver_Entry.grid(row = 1,column = 4,sticky=customtkinter.N,pady = 20)
    self.Driver_Import.grid(row = 1,column = 5,sticky=customtkinter.N,pady = 20,padx=10)