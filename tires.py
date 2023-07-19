from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from utils import check_tire_wear


class Tires:
    def __init__(self, strategy: TireType) -> None:

        self._strategy = strategy

    
    @property
    def strategy(self) -> TireType:

        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: TireType) -> None:

        self._strategy = strategy

    def tires_should_be_serviced(self) -> bool:
        result = self._strategy.needs_service()
        return result

class TireType(ABC):

    @abstractmethod
    def needs_service(self):
        pass


class CarriganTires(TireType):
    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self):
        single_tire_wear_threshold = 0.9
        tire_wears = [check_tire_wear(i, single_tire_wear_threshold) for i in self.tire_wear_sensors]
        return any(tire_wears)
    

class OctoprimeTires(TireType):
    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self):
        combined_tire_wears_threshold = 3
        return sum(self.tire_wear_sensors) >= combined_tire_wears_threshold
