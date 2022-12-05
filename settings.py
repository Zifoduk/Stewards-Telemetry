import os
from pathlib import Path
import yaml
from yaml import Loader


SETTINGS_YAML = open("settings.yml", "r")
SETTINGS_DATA = yaml.load(SETTINGS_YAML, Loader=Loader)



def GetDataPath():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), Path("Data/"))
def GetDataFilePath(file):
    return os.path.join(GetDataPath(), Path(file))

def GetResourcesPath():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), Path("Resources/"))
def GetImagePath():
    return os.path.join(GetResourcesPath(), Path("Images/"))
def GetImageFilePath(file):
    return os.path.join(GetResourcesPath(), Path("Images/"), Path(file))
def GetThemesPath():
    return os.path.join(GetResourcesPath(), Path("Themes/"))
def GetThemesFilePath(file):
    return os.path.join(GetResourcesPath(), Path("Themes/"),  Path(file))


# def GetdbPath():
#     return os.path.join(os.path.dirname(os.path.abspath(__file__)), Path("dbs/"))


# def GetTestGuilds():
#     return SETTINGS_DATA["TestGuilds"]
