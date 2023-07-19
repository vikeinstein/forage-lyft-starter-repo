from __future__ import annotations
from abc import ABC, abstractmethod
from engine import Engine, CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import Battery, SpindlerBattery, NubbinBattery
from tire import Tires, CarriganTires, OctoprimeTires
from datetime import datetime

        
class CarFactory(ABC):

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
        engine = Engine(CapuletEngine(current_mileage, last_service_mileage))
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        tires =  Tires(CarriganTires(tire_wear_sensors))
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
        engine = Engine(WilloughbyEngine(current_mileage, last_service_mileage))
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        tires =  Tires(CarriganTires(tire_wear_sensors))
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear_sensors):
        engine = Engine(SternmanEngine(warning_light_on))
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        tires =  Tires(CarriganTires(tire_wear_sensors))
        car = Car(engine, battery, tires)
        return car
       
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
        engine = Engine(WilloughbyEngine(current_mileage, last_service_mileage))
        battery = Battery(NubbinBattery(last_service_date, current_date))
        tires =  Tires(OctoprimeTires(tire_wear_sensors))
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
        engine = Engine(CapuletEngine(current_mileage, last_service_mileage))
        battery = Battery(NubbinBattery(last_service_date, current_date))
        tires =  Tires(OctoprimeTires(tire_wear_sensors))        
        car = Car(engine, battery, tires)
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
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced() or \
        self.tires.tires_should_be_serviced()
