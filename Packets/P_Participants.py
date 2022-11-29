from . import BasePacket
from datetime import datetime
class P_Participants(BasePacket):
    def __init__(self, packet):
        super().__init__(packet)
        self.Analyse()
        self.timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S%f")
        
    def Analyse(self):
        self.List_Participants = [participant.to_dict() for participant in self.rawPacket.participants]
        print(type(self.List_Participants))
