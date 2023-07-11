from engine import Engine,  CapuletEngine, SternmanEngine
from datetime import datetime
from battery import Battery, SpindlerBattery, NubbinBattery
from car_factory import CarFactory


if __name__ == "__main__":


    current_mileage = 50000
    last_service_mileage = 0
    warning_light_on = False
    current_date = datetime.today().date()
    last_service_date = current_date.replace(year=current_date.year - 1)


    engine1 = Engine(CapuletEngine(current_mileage, last_service_mileage))
    engine_check1 = engine1.engine_should_be_serviced()
    print(engine_check1)

    engine2 = Engine(SternmanEngine(warning_light_on))
    engine_check2 = engine2.engine_should_be_serviced()
    print(engine_check2)


    battery1 = Battery(SpindlerBattery(last_service_date, current_date))
    battery_check1= battery1.battery_should_be_serviced()
    print(battery_check1)

    battery2 = Battery(SpindlerBattery(last_service_date, current_date))
    battery_check2 = battery2.battery_should_be_serviced()
    print(battery_check2)