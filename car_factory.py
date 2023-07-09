from __future__ import annotations
from abc import ABC, abstractmethod
from engine import Engine, CapuletEngine 
from battery import Battery, SpindlerBattery

        
class CarFactory(ABC):

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine(CapuletEngine(current_mileage, last_service_mileage))
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        car = Car(engine, battery)
        return car

class Serviceable(ABC):
    """
    The Serviceable interface declares operations that all concrete products (cars)
    must implement.
    Cars are accessed through the Serviceable interface
    """
    @abstractmethod
    def needs_service(self):
        pass


class Car(Serviceable):
    def __init__(self, engine = None, battery = None):
        self._engine = engine
        self._battery = battery

    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced()