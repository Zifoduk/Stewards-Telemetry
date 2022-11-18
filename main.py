from f1_22_telemetry.listener import TelemetryListener
import json
from Packets import Packet
import multiprocessing
import asyncio


listener = TelemetryListener(port=20779, host='localhost')

race_director = {"participants": [], "events":[]}

obtained = False

async def AddRaceDirector(packet):
    print(packet.ESC)
    if packet.ESC not in ["SPTP", "RCWN", "TMPT", "FLBK", "BUTN"]:
        print(packet.data.to_dict())
        race_director["events"].append(packet.data.to_dict())
        len(race_director["events"])

 
async def main():
    while True:
        packet = listener.get()
        if packet.header.packet_id == 3:
                p = Packet.getPacket(packet)
                await AddRaceDirector(p)
                #RDAThread = multiprocessing.Process(target=AddRaceDirector, args=(p,))
                #RDAThread.start()


            # packet = packet.to_dict()
            # #print(packet["PacketEventData"]["penalty"])
            # esc = packet["event_string_code"]
            # esc = "".join([chr(i) for i in esc])
            #print(packet["event_string_code"])
            # if esc != "BUTN":
            #     print(esc)
            
            # if esc == "SPTP":
            #     SPTPPack = packet["event_details"]["speed_trap"]
            #     print("VID: ", SPTPPack["vehicle_idx"], "Spud: ", SPTPPack["speed"])
            #     with open("test.txt", "a") as myfile:
            #         myfile.write(f'\nVID: {SPTPPack["vehicle_idx"]} Spud: {SPTPPack["speed"]}') 

            # if esc == "PENA":
            #     PenPack = packet["event_details"]["penalty"]
            #     PenPack["timestamp"] = datetime.now().strftime("%d-%m-%Y, %H:%M:%S%f")
            #     race_director["events"].append(PenPack)
            #     print("VID: ", PenPack["vehicle_idx"], "PT: ", PenPack["penalty_type"], "IT: ", PenPack["infringement_type"], "OVID: ", PenPack["other_vehicle_idx"])
            # continue
        
        # if packet.header.packet_id == 4 and not obtained:
        #     packet = packet.to_dict()
        #     ppd = packet["participants"]
        #     race_director["participants"] = ppd
        #     obtained = True
        #     continue

try:   
    asyncio.run(main())
except KeyboardInterrupt:
    print("Program terminated manually!")
    with open("sample.json", "w") as outfile:
        json.dump(race_director, outfile)
    raise SystemExit