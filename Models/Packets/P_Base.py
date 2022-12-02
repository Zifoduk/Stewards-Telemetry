from abc import ABC, abstractmethod

class BasePacket(ABC):
    def __init__(self, packet):
        self.rawPacket = packet
        self.header = packet.header

    @property
    def PacketType(self):
        return f"{PACKET_ID_TO_PACKET_TYPE_NAME[self.header.id]}"
        

PACKET_ID_TO_PACKET_TYPE_NAME = {
    0:"MOTION",
    1:"SESSION",
    2:"LAP_DATA",
    3:"EVENT",
    4:"PARTICIPANTS",
    5:"CAR_SETUPS",
    6:"CAR_TELEMETRY",
    7:"CAR_STATUS",
    8:"FINAL_CLASSIFICATION",
    9:"LOBBY_INFO",
    10:"CAR_DAMAGE",
    11:"SESSION_HISTORY"
}