from f1_22_telemetry.listener import TelemetryListener
import json
from Packets import Packet
import multiprocessing
import asyncio


listener = TelemetryListener(port=20779, host='localhost')

race_director = {"participants": [], "events":[]}

obtained = False

async def AddRaceDirector(packet):
    if packet.ESC not in ["SPTP", "RCWN", "TMPT", "FLBK", "BUTN"]:
        print(packet.ESC, " appened")
        race_director["events"].append(packet.data.to_dict())

 
async def main():
    obtained = False
    while True:
        packet = listener.get()
        if packet.header.packet_id == 3:
                p = Packet.getPacket(packet)
                await AddRaceDirector(p)
        
        if packet.header.packet_id == 4 and not obtained:
            packet = packet.to_dict()
            ppd = packet["participants"]
            race_director["participants"] = ppd
            obtained = True
            continue

try:   
    asyncio.run(main())
except KeyboardInterrupt:
    print("Program terminated manually!")
    with open("sample.json", "w") as outfile:
        json.dump(race_director, outfile)
    raise SystemExit