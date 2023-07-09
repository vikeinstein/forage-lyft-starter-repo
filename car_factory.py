from __future__ import annotations
from abc import ABC, abstractmethod
from engine import Engine, CapuletEngine
from battery import Battery, SpindlerBattery
#from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
#from battery import SpindlerBattery, NubbinBattery
from datetime import datetime

        
class CarFactory(ABC):

    @abstractmethod
    def create_calliope(self):
        pass

    """
    @abstractmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        pass

    @abstractmethod
    def create_glissade(self) -> Car:
        pass

    @abstractmethod
    def create_palindrome(self) -> Car:
        pass

    @abstractmethod
    def create_rorschach(self) -> Car:
        pass

    @abstractmethod
    def create_thovex(self) -> Car:
        pass
    """

    def some_operation(self) -> bool:
        
        calliope = self.create_calliope()

        return calliope.needs_service()

    
    
class CalliopeFactory(CarFactory):
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        self._current_date = current_date
        self._last_service_date = last_service_date
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

        return Calliope()


class IServiceable(ABC):
    """
    The Serviceable interface declares operations that all concrete products (cars)
    must implement.
    Cars are accessed through the Serviceable interface
    """
    @abstractmethod
    def needs_service(self):
        pass


class Car(IServiceable):
    def __init__(self, engine = None, battery = None):
        self._engine = engine
        self._battery = battery

    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced()

   
class Calliope(Car):
    def __init__(self, current_date = None, last_service_date = None,\
                  current_mileage = None, last_service_mileage = None) -> Car:
        Car.__init__(self, engine = Engine(CapuletEngine(self.current_mileage, self.last_service_mileage)))
        Car.__init__(self, battery = Battery(SpindlerBattery(self.last_service_date, self.current_date)))
        self._current_date = current_date
        self._last_service_date = last_service_date
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage


if __name__ == "__main__":
    current_mileage = 20000
    last_service_mileage = 0
    today = datetime.today().date()
    current_date = today
    last_service_date = today.replace(year=today.year - 1)
    calliope = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    print(calliope.some_operation())


