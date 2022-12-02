from f1_22_telemetry.listener import TelemetryListener
import json
from Models.Packets import Packet
import multiprocessing
import asyncio
from multipledispatch import dispatch
import globalVars
import socket
import time
import queue
import threading

class TelemetryService(threading.Thread):
    def __init__(self):
        self.listener = TelemetryListener(port=20779, host='localhost')
        self.race_director = {"participants": [], "events":[], "final_classification": []}
        self.obtained = False
        asyncio.run(self.main())

    async def AddFinalClassification(self, packet):
        self.race_director["final_classification"] = packet.Classification

    async def AddRaceDirector(self, packet):
        if packet.ESC not in ["SPTP", "RCWN", "TMPT", "FLBK", "BUTN"]:
            print(packet.ESC, " appened")
            if packet.data != None:
                self.race_director["events"].append(packet.data.to_dict())
    
    async def AddParticipants(self, packet):
        self.race_director["participants"] = packet.List_Participants

    async def main(self):        
        try:   
            while globalVars.app_Open:
                if globalVars.activated:
                    try:
                        _packet = self.listener.get()  
                    except socket.timeout:
                        time.sleep(1)
                        continue
                    packet = Packet.getPacket(_packet)
                    if packet != None:
                        try:
                            for route in self.PACKET_ID_ROUTE[packet.header.packet_id]:
                                await route(packet)
                        except Exception as e:
                            print(e)
                            
                time.sleep(0.5)
        except e:
            pass
        finally:
            print("Program terminated manually!")
            with open("sample.json", "w") as outfile:
                json.dump(self.race_director, outfile)
            raise SystemExit


    PACKET_ID_ROUTE={
        0:"",
        1:[AddRaceDirector],
        2:"",
        3:[AddRaceDirector],
        4:[AddParticipants],
        5:"",
        6:"",
        7:"",
        8:[AddFinalClassification],
        9:[AddRaceDirector],
        10:"",
        11:[AddRaceDirector]
        }



    