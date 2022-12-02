import customtkinter
from Utilities import Util_ViewThemes as UVT
from Views import View_MainFrame
import globalVars
from Services.TelemetryService import TelemetryService
from threading import Thread
import time

telemetryService = Thread(target=TelemetryService)
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
#customtkinter.set_default_color_theme('Resources\Themes\green.json')  # Themes: "blue" (standard), "green", "dark-blue"

if __name__ == "__main__":
    app = View_MainFrame.MainFrame()
    globalVars.initialize()    
    telemetryService.start()
    app.mainloop()