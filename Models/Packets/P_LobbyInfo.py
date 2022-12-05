from . import BasePacket
from datetime import datetime
class P_LobbyInfo(BasePacket):
    def __init__(self, packet):
        super().__init__(packet)
        self.Analyse()
        self.timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S%f")
        
    def Analyse(self):
        self.Lobby_Players = [Player.to_dict() for Player in self.rawPacket.lobby_players]
