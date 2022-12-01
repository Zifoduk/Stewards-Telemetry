import tkinter
import tkinter.messagebox
import customtkinter
import os
from PIL import Image, ImageTk

Themes_List ={}
for filename in os.listdir('./Themes'):
    Themes_List[filename[:-5]]= f'Themes\{filename}'




customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(Themes_List['blue'])  # Themes: "blue" (standard), "green", "dark-blue"




class MainFrame(customtkinter.CTk):

    WIDTH = 1280   
    HEIGHT = 720

    global Menu_State
    Menu_State = False

    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{MainFrame.WIDTH}x{MainFrame.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
 

        # ============ frame_left ============



        self.frame_1 = customtkinter.CTkFrame(self, width=20,corner_radius=15)
        self.frame_1.grid(row=0, column=0, padx=20, pady=20,sticky='n')

        self.pg1 = customtkinter.CTkButton(self.frame_1,text='',image=ImageTk.PhotoImage(Image.open('Images\Menu.png').resize((20, 20))),height=30,width=30,command=self.Menu)
        self.pg1.grid(row=1, column=0,padx=10,pady=10,sticky='w')

        self.pg1 = customtkinter.CTkButton(self.frame_1,text='',height=30,width=30)
        self.pg1.grid(row=3, column=0,padx=10,pady=10)

        self.pg2 = customtkinter.CTkButton(self.frame_1,text='',image=ImageTk.PhotoImage(Image.open('Images\People_Icon.png').resize((20, 20))),height=30,width=30,command=self.People)
        self.pg2.grid(row=5, column=0,padx=10,pady=10)

        self.pg3 = customtkinter.CTkButton(self.frame_1,text='',image=ImageTk.PhotoImage(Image.open('Images\RaceDirector.png').resize((20, 20))),height=30,width=30,command=self.RD_Page)
        self.pg3.grid(row=7, column=0,padx=10,pady=10)

        self.pg4 = customtkinter.CTkButton(self.frame_1,text='',image=ImageTk.PhotoImage(Image.open('Images\Settings.png').resize((20, 20))),height=30,width=30,command=self.Settings_Window)
        self.pg4.grid(row=9, column=0,padx=10,pady=10)

        

        # ============ frame_right ============

        self.frame_2 = customtkinter.CTkFrame(self,width=500,height=MainFrame.HEIGHT-40)
        self.frame_2.grid(row=0,column=1,pady=20,sticky='news')


    def Menu(self):
        global Menu_State
        if Menu_State is False:
            self.pg1.configure(text= 'Home',width=100,image=None)
            self.pg2.configure(text= 'Players',width=100,image=None)
            self.pg3.configure(text= 'Race Director',width=100,image=None)
            self.pg4.configure(text= 'Settings',width=100,image=None)
            
            Menu_State = True        
        else:
            self.pg1.configure(text='',width=30)
            self.pg2.configure(text='',width=30,image=ImageTk.PhotoImage(Image.open('Images\People_Icon.png').resize((20, 20))))
            self.pg3.configure(text='',width=30,image=ImageTk.PhotoImage(Image.open('Images\RaceDirector.png').resize((20, 20))))
            self.pg4.configure(text='',width=30,image=ImageTk.PhotoImage(Image.open('Images\Settings.png').resize((20, 20))))
            Menu_State = False


    def People(self):

        for widget in self.frame_2.winfo_children():
            widget.grid_forget()  
        
        self.frame_4 = customtkinter.CTkFrame(self.frame_2,width=800)
        self.frame_4.grid(row=0,column=1,padx=20,pady=20,sticky='news')

        self.label = customtkinter.CTkLabel(self.frame_4,text='Player Data',width=800)
        self.label.grid(row=1, column=0,padx=10,pady=10)

    def RD_Page(self):

        for widget in self.frame_2.winfo_children():
            widget.grid_forget() 

        self.frame_5 = customtkinter.CTkFrame(self.frame_2,width=500)
        self.frame_5.grid(row=0,column=1,padx=20,pady=20,sticky='news')


        self.label = customtkinter.CTkLabel(self.frame_5,text='Race Director',width=800)
        self.label.grid(row=1, column=0,padx=10,pady=10)


    def Settings_Window(self):

        Width = 900
        Height = 600


        window = customtkinter.CTkToplevel(self)
        window.geometry(f'{Width}x{Height}')

        window_frame = customtkinter.CTkFrame(window,width=Width-40,height=Height-40,corner_radius=15)
        window_frame.grid(row=0,column=0,padx=20,pady=10)

        window_title = customtkinter.CTkLabel(window_frame,text="Settings",width=Width-40,height=10)
        window_title.grid(row=0,column=0,pady=10)



        window_content_frame = customtkinter.CTkFrame(window,width=Width-40,height=200,corner_radius=15)
        window_content_frame.grid(row=1,column=0,padx=20,sticky=customtkinter.W)

        window_content_frame.columnconfigure(0, weight=1)
        window_content_frame.columnconfigure(1, weight=3)

        global switch_var 
        switch_var = customtkinter.StringVar(value="dark")

        switch_1 = customtkinter.CTkSwitch(master=window_content_frame, text="Screen Mode",command=self.switch_event,variable=switch_var, onvalue="light", offvalue="dark")
        switch_1.grid(row=10,column=0,padx=20,pady=20,sticky=customtkinter.W)

        IP_Label = customtkinter.CTkLabel(window_content_frame,text='IP Address',width=100,height=10)
        IP_Label.grid(row=0,column=2,padx=20,pady=20,sticky=customtkinter.E)

        IP_Label = customtkinter.CTkLabel(window_content_frame,text='Port',width=100,height=10)
        IP_Label.grid(row=1,column=2,padx=20,pady=20,sticky=customtkinter.E)

        IP_Address = customtkinter.CTkEntry(master=window_content_frame,
                               placeholder_text="127.0.0.1",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
        Port_Address = customtkinter.CTkEntry(master=window_content_frame,
                               placeholder_text="20777",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
        
        IP_Address.grid(row=0,column=3,columnspan=2,padx=20,pady=20,sticky=customtkinter.E)
        Port_Address.grid(row=1,column=3,columnspan=2,padx=20,pady=20,sticky=customtkinter.E)
        




    def switch_event(self):
        customtkinter.set_appearance_mode(switch_var.get())  # Modes: "System" (standard), "Dark", "Light"









    def on_closing(self, event=0):
        self.destroy()





if __name__ == "__main__":
    app = MainFrame()
    app.mainloop()