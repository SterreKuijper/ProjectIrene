from utils.functions import celsius_to_kelvin
from utils.constants import Constants

class Environment:
    def __init__(self, amb_pressure, amb_temperature_C):
        self.amb_pressure = amb_pressure
        self.amb_temperature_C = amb_temperature_C
        self.amb_temperature_K = celsius_to_kelvin(amb_temperature_C)
        # TODO: add constants for the other values or make it clear what the formula does
        self.air_density = (amb_pressure * 100) / (Constants.SPECIFIC_GAS_CONSTANT_AIR * (amb_pressure + 273.15))

