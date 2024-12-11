from utils.functions import celsius_to_kelvin


class Environment:
    def __init__(self, amb_pressure, amb_temperature_C):
        self.amb_pressure = amb_pressure
        self.amb_temperature_C = amb_temperature_C
        self.amb_temperature_K = celsius_to_kelvin(amb_temperature_C)
