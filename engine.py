from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime


class Engine:
    def __init__(self, strategy: EngineType) -> None:

        self._strategy = strategy

    
    @property
    def strategy(self) -> EngineType:

        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: EngineType) -> None:

        self._strategy = strategy

    def engine_should_be_serviced(self) -> bool:
        result = self._strategy.needs_service()
        return result

class EngineType(ABC):

    @abstractmethod
    def needs_service(self):
        pass


class CapuletEngine(EngineType):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
    

class SternmanEngine(EngineType):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        if self.warning_light_on:
            return True
        else:
            return False
        

class WilloughbyEngine(EngineType):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
