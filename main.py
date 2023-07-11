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

    def print_needs_service(car_model, needs_service):
        statement = 'does not need'
        if needs_service == True:
            statement = 'needs'
 
        print(f'{car_model} {statement} service')


    calliope = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    print_needs_service('Calliope', calliope.needs_service())

    glissade = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
    print_needs_service('Calliope', glissade.needs_service())

    palindrome = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on)
    print_needs_service('Palindrome', palindrome.needs_service())

    rorschach = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
    print_needs_service('Rorschach', rorschach.needs_service())

    thovex = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
    print_needs_service('Thovex', thovex.needs_service())