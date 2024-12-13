from utils.functions import celsius_to_kelvin
from utils.constants import Constants

class Environment:
    """
        Represents the environmental parameters relevant to air density calculations.

        Attributes:
            amb_pressure (float): Ambient pressure in Pascals (Pa).
            amb_temperature_C (float): Ambient temperature in degrees Celsius (°C).
            amb_temperature_K (float): Ambient temperature in Kelvin (K).
            air_density (float): Calculated air density in kilograms per cubic meter (kg/m³).
        """

    def __init__(self, amb_pressure, amb_temperature_C):
        self.amb_pressure = amb_pressure
        self.amb_temperature_C = amb_temperature_C
        self.amb_temperature_K = celsius_to_kelvin(amb_temperature_C)

        self.air_density = amb_pressure / (Constants.SPECIFIC_GAS_CONSTANT_AIR * amb_temperature_C)