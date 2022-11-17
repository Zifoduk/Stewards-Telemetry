from f1_22_telemetry.listener import TelemetryListener
import json
from datetime import datetime

listener = TelemetryListener(port=20777, host='localhost')

race_director = {"participants": [], "events":[]}

obtained = False
try:
    while True:
        packet = listener.get()
        if packet.header.packet_id == 3:
            packet = packet.to_dict()
            #print(packet["PacketEventData"]["penalty"])
            esc = packet["event_string_code"]
            esc = "".join([chr(i) for i in esc])
            #print(packet["event_string_code"])
            if esc != "BUTN":
                print(esc)
            
            if esc == "SPTP":
                SPTPPack = packet["event_details"]["speed_trap"]
                print("VID: ", SPTPPack["vehicle_idx"], "Spud: ", SPTPPack["speed"])
                with open("test.txt", "a") as myfile:
                    myfile.write(f'\nVID: {SPTPPack["vehicle_idx"]} Spud: {SPTPPack["speed"]}') 

            if esc == "PENA":
                PenPack = packet["event_details"]["penalty"]
                PenPack["timestamp"] = datetime.now().strftime("%d-%m-%Y, %H:%M:%S%f")
                race_director["events"].append(PenPack)
                print("VID: ", PenPack["vehicle_idx"], "PT: ", PenPack["penalty_type"], "IT: ", PenPack["infringement_type"], "OVID: ", PenPack["other_vehicle_idx"])
            continue
        
        if packet.header.packet_id == 4 and not obtained:
            packet = packet.to_dict()
            ppd = packet["participants"]
            race_director["participants"] = ppd
            obtained = True
            continue

except KeyboardInterrupt:
    print("Program terminated manually!")
    with open("sample.json", "w") as outfile:
        json.dump(race_director, outfile)
    raise SystemExit