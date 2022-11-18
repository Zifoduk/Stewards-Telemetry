from . import BasePacket
from datetime import datetime
class P_EventData(BasePacket):
    def __init__(self, packet):
        super().__init__(packet)
        self.ESC = "".join([chr(i) for i in packet.event_string_code])
        self.Analyse()
        self.timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S%f")
        
    def Analyse(self):
        route = ESC_TO_EVENT_DETAIL[self.ESC]
        if route != "":
            self.data = getattr(self.rawPacket.event_details, route)

    @property
    def Penalty():
        return {}

    def SpeedTrap():        
        pass
    
ESC_TO_EVENT_DETAIL = {
    "SSTA":"",
    "SEND":"",
    "FTLP":"fastest_lap",
    "RTMT":"retirement",
    "DRSE":"",
    "DRSD":"",
    "TMPT":"team_mate_in_pits",
    "CHQF":"",
    "RCWN":"race_winner",
    "PENA":"penalty",
    "SPTP":"speed_trap",
    "STLG":"start_lights",
    "LGOT":"",
    "DTSV":"drive_through_penalty_served",
    "SGSV":"stop_go_penalty_served",
    "FLBK":"flashback",
    "BUTN":"buttons"
}