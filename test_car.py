import unittest
from datetime import datetime

from engine import Engine,  CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import Battery, SpindlerBattery, NubbinBattery



class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        self.assertTrue(battery.battery_should_be_serviced())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        self.assertFalse(battery.battery_should_be_serviced())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = Engine(CapuletEngine(current_mileage, last_service_mileage))
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = Engine(CapuletEngine(current_mileage, last_service_mileage))
        self.assertFalse(engine.engine_should_be_serviced())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        self.assertTrue(battery.battery_should_be_serviced())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        self.assertFalse(battery.battery_should_be_serviced())

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = Engine(WilloughbyEngine(current_mileage, last_service_mileage))
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = Engine(WilloughbyEngine(current_mileage, last_service_mileage))
        self.assertFalse(engine.engine_should_be_serviced())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        self.assertTrue(battery.battery_should_be_serviced())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = Battery(SpindlerBattery(last_service_date, current_date))
        self.assertFalse(battery.battery_should_be_serviced())

    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = Engine(SternmanEngine(warning_light_is_on))
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = Engine(SternmanEngine(warning_light_is_on))
        self.assertFalse(engine.engine_should_be_serviced())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        battery = Battery(NubbinBattery(last_service_date, current_date))
        self.assertTrue(battery.battery_should_be_serviced())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = Battery(NubbinBattery(last_service_date, current_date))
        self.assertFalse(battery.battery_should_be_serviced())

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = Engine(WilloughbyEngine(current_mileage, last_service_mileage))
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = Engine(WilloughbyEngine(current_mileage, last_service_mileage))
        self.assertFalse(engine.engine_should_be_serviced())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        battery = Battery(NubbinBattery(last_service_date, current_date))
        self.assertTrue(battery.battery_should_be_serviced())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = Battery(NubbinBattery(last_service_date, current_date))
        self.assertFalse(battery.battery_should_be_serviced())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = Engine(CapuletEngine(current_mileage, last_service_mileage))
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = Engine(CapuletEngine(current_mileage, last_service_mileage))
        self.assertFalse(engine.engine_should_be_serviced())


if __name__ == '__main__':
    unittest.main()
