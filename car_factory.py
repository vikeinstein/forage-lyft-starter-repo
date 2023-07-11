from __future__ import annotations
from abc import ABC, abstractmethod
from engine import Engine, CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import Battery, SpindlerBattery, NubbinBattery
from datetime import datetime

        
class CarFactory(ABC):

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine(CapuletEngine(current_mileage, last_service_mileage))
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine(WilloughbyEngine(current_mileage, last_service_mileage))
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = Engine(SternmanEngine(warning_light_on))
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        car = Car(engine, battery)
        return car
       
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine(WilloughbyEngine(current_mileage, last_service_mileage))
        battery = Battery(NubbinBattery(last_service_date, current_date))
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine(CapuletEngine(current_mileage, last_service_mileage))
        battery = Battery(NubbinBattery(last_service_date, current_date))
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
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced()
