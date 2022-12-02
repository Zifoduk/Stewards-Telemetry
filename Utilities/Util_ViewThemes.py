import os
import settings

Themes_List ={}
for filename in os.listdir(settings.GetThemesPath()):
    Themes_List[filename[:-5]]= settings.GetThemesFilePath(filename)