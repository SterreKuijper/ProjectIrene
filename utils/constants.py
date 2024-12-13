import math

class Constants:
    """
    Constant class that contains static variables
    """
    MM_PER_INCH = 25.4
    KELVIN_CELSIUS_OFFSET = 273.15 # K
    ROLLING_RESISTANCE_COEFFICIENT = 0.02 # (Motorcycle Dynamics - Vittore Cossalter)
    DRAG_COEFFICIENT = 0.7 # C_D*A ~ 0.3-0.35 for racing motorcycles with A ~ 0.5 (Motorcycle Dynamics - Vittore Cossalter)
    LIFT_COEFFICIENT = 0.12 # C_L*A ~ 0.06-0.12 for racing motorcycles with A ~ 0.5 (Motorcycle Dynamics - Vittore Cossalter)
    SPECIFIC_GAS_CONSTANT_AIR = 287.05 # J/(kg*K)
    GRAVITATIONAL_ACCELERATION = math.pow(math.pi, 2) # ms^-2
    GEAR_EFFICIENCY = 0.98