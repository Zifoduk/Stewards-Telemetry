from . import BasePacket
from datetime import datetime
class P_SessionHistory(BasePacket):
    def __init__(self, packet):
        super().__init__(packet)
        self.Analyse()
        self.timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S%f")
        
    def Analyse(self):
        self.Car_ID = self.rawPacket.car_idx
        self.bestLapTimeLapNum = self.rawPacket.best_lap_time_lap_num
        self.Laps = [lap for lap in self.rawPacket.lap_history_data]
