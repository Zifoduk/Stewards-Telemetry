import customtkinter
from settings import GetImageFilePath
from . import View_People, View_Race_Director, View_Settings
from PIL import Image, ImageTk
import globalVars

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
 
        # ============ frame_right ============

        self.frame_2 = customtkinter.CTkFrame(self,width=500,height=MainFrame.HEIGHT-40)
        self.frame_2.grid(row=0,column=1,pady=20,sticky='news')

        # ============ frame_left ============

        self.frame_1 = customtkinter.CTkFrame(self, width=20,corner_radius=15)
        self.frame_1.grid(row=0, column=0, padx=20, pady=20,sticky='n')

        self.pg1 = customtkinter.CTkButton(self.frame_1,text='',height=30,width=30,command=self.Menu)
        self.pg1.grid(row=1, column=0,padx=10,pady=10,sticky='w')

        self.pg1 = customtkinter.CTkButton(self.frame_1,text='',height=30,width=30)
        self.pg1.grid(row=3, column=0,padx=10,pady=10)

        self.pg2 = customtkinter.CTkButton(self.frame_1,text='',height=30,width=30,command=lambda: self.Handle_Menu_Change("People"))
        self.pg2.grid(row=5, column=0,padx=10,pady=10)

        self.pg3 = customtkinter.CTkButton(self.frame_1,text='',height=30,width=30,command=lambda: self.Handle_Menu_Change("Race Director"))
        self.pg3.grid(row=7, column=0,padx=10,pady=10)

        self.pg4 = customtkinter.CTkButton(self.frame_1,text='',height=30,width=30,command=lambda: self.Handle_Menu_Change("Settings"))
        self.pg4.grid(row=9, column=0,padx=10,pady=10)

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
            self.pg2.configure(text='',width=30)
            self.pg3.configure(text='',width=30)
            self.pg4.configure(text='',width=30)
            Menu_State = False

    def Handle_Menu_Change(self, page):
        for widget in self.frame_2.winfo_children():
            widget.grid_forget()

        route = self.LIST_OF_PAGES[page]
        route(self, self.frame_2)

    def on_closing(self, event=0):
        globalVars.app_Open = False
        self.destroy()

    LIST_OF_PAGES = {
        "Settings": View_Settings.Settings,
        "People": View_People.People,
        "Race Director": View_Race_Director.Race_Director,
    }

def ButtonIcons(filename):
    return Image.open('Resources\Images\People_Icon.png').resize((20, 20))
    #return GetImageFilePath(filename)
    #return Image.open(GetImageFilePath(filename)).resize((20, 20))