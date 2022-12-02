from . import BasePacket
from datetime import datetime
class P_FinalClassification(BasePacket):
    def __init__(self, packet):
        super().__init__(packet)
        self.Analyse()
        self.NumberOfCars = self.rawPacket.num_cars    
        self.timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S%f")
        
    def Analyse(self):
        TYRE_ID_TO_COMPOUND = {
            "0": None,
            "7": "Inter",
            "8": "Wet",
            "16": "C5",
            "17": "C4",
            "18": "C3",
            "19": "C2",
            "20": "C1"
        }

        TYRE_ID_TO_VISUAL_COMPOUND = {
            "0": None,
            "7": "Inter",
            "8": "Wet",
            "16": "Soft",
            "17": "Medium",
            "18": "Hard"
        }    
        self.Classification = []
        for car in self.rawPacket.classification_data:
            car_data = {"Position": car.position,
                        "Laps_Completed": car.num_laps,
                        "Grid_Position": car.grid_position,
                        "Points": car.points,
                        "Pitstops": car.num_pit_stops,
                        "Status": car.result_status,
                        "Fastest_lap": car.best_lap_time_in_ms,
                        "Penalties_Time": car.penalties_time,
                        "Penalties": car.num_penalties,
                        "Tyre_Stints": car.num_tyre_stints,
                        "Tyre_Stints_Actual": [TYRE_ID_TO_COMPOUND[str(val)] for val in car.tyre_stints_actual if val != 0],
                        "Tyre_Stints_Visual": [TYRE_ID_TO_VISUAL_COMPOUND[str(val)] for val in car.tyre_stints_visual if val != 0],
                        "Tyre_Stints_End_Laps": [val for val in car.tyre_stints_end_laps]
                        }
            self.Classification.append(car_data)

        