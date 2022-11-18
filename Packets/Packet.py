from . import *

def getPacket(packet):
    p_class = PACKET_ID_TO_PACKET_TYPE[packet.header.packet_id]
    return p_class(packet)

PACKET_ID_TO_PACKET_TYPE = {
    0:P_Motion,
    1:"SESSION",
    2:"LAP_DATA",
    3:P_EventData,
    4:"PARTICIPANTS",
    5:"CAR_SETUPS",
    6:"CAR_TELEMETRY",
    7:"CAR_STATUS",
    8:"FINAL_CLASSIFICATION",
    9:"LOBBY_INFO",
    10:"CAR_DAMAGE",
    11:"SESSION_HISTORY"
}