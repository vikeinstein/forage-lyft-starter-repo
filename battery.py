from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime


class Battery:
    def __init__(self, strategy: BatteryType) -> None:

        self._strategy = strategy

    
    @property
    def strategy(self) -> BatteryType:

        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: BatteryType) -> None:

        self._strategy = strategy

    def battery_should_be_serviced(self) -> bool:
        result = self._strategy.needs_service()
        return result

class BatteryType(ABC):

    @abstractmethod
    def needs_service(self):
        pass


class SpindlerBattery(BatteryType):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return service_threshold_date < self.current_date
    

class NubbinBattery(BatteryType):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < self.current_date
