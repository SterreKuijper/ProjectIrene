import math

class Constants:
    """
    Constant class that contains static variables
    """
    MM_PER_INCH = 25.4
    KELVIN_CELSIUS_OFFSET = 273.15 # K
    ROLLING_COEFFICIENT = 0.02
    DRAG_COEFFICIENT = 0.61
    LIFT_COEFFICIENT = 0.02
    SPECIFIC_GAS_CONSTANT_AIR = 28.964917 # g/mol
    GRAVITATIONAL_ACCELERATION = math.pow(math.pi, 2) # ms^-2
    GEAR_EFFICIENCY = 0.98