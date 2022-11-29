from f1_22_telemetry.listener import TelemetryListener
import json
from Packets import Packet
import multiprocessing
import asyncio
from multipledispatch import dispatch

listener = TelemetryListener(port=20779, host='localhost')

race_director = {"participants": [], "events":[], "final_classification": []}

global obtained
obtained = False

async def AddFinalClassification(packet):
    race_director["final_classification"] = packet.Classification

async def AddRaceDirector(packet):
    if packet.ESC not in ["SPTP", "RCWN", "TMPT", "FLBK", "BUTN"]:
        print(packet.ESC, " appened")
        if packet.data != None:
            race_director["events"].append(packet.data.to_dict())
 
async def AddParticipants(packet):
    race_director["participants"] = packet.List_Participants

async def main():
    while True:
        _packet = listener.get()        
        packet = Packet.getPacket(_packet)
        if packet != None:
            try:
                for route in PACKET_ID_ROUTE[packet.header.packet_id]:
                    await route(packet)
            except Exception as e:
                print(e)


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

try:   
    asyncio.run(main())
except KeyboardInterrupt:
    print("Program terminated manually!")
    with open("sample.json", "w") as outfile:
        json.dump(race_director, outfile)
    raise SystemExit


    