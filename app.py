import customtkinter
from Utilities import Util_ViewThemes as UVT
from Views import View_MainFrame
import globalVars
from Services.TelemetryService import TelemetryService
from threading import Thread
import time
import json
telemetryService = Thread(target=TelemetryService)

appearence_mode = 'Dark'
Theme = 'red'

global Theme_Dict
Theme_Dict = json.load(open(UVT.Themes_List[Theme]))

global Theme_Mode
Theme_Mode = 1

customtkinter.set_appearance_mode(appearence_mode)  
customtkinter.set_default_color_theme(UVT.Themes_List[Theme])  

if __name__ == "__main__":
    app = View_MainFrame.MainFrame()
    globalVars.initialize()    
    telemetryService.start()
    app.mainloop()