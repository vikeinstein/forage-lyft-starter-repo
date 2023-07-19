def check_tire_wear(tire_wear_sensor, threshold):
    if (tire_wear_sensor >= 0) and (tire_wear_sensor <= 1):
        return tire_wear_sensor >= threshold
