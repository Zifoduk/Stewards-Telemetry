import customtkinter
from Utilities import Util_ViewThemes as UVT
from Views import View_MainFrame

global activated
activated = False

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme(UVT.Themes_List['blue'])  # Themes: "blue" (standard), "green", "dark-blue"

if __name__ == "__main__":
    app = View_MainFrame.MainFrame()
    app.mainloop()