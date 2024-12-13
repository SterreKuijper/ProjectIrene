import math
from utils.functions import inch_to_mm
from utils.constants import Constants


class Wheel:

    def __init__(self, width, aspect_ratio, rim_diameter_inch):
        self.width = width
        self.aspect_ratio = aspect_ratio
        self.rim_diameter_inch = rim_diameter_inch
        self.rim_diameter_mm = inch_to_mm(rim_diameter_inch)

        self.crown_radius = width * aspect_ratio
        self.diameter = self.rim_diameter_mm + 2 * self.crown_radius
        self.circumference = self.diameter * math.pi
        self.radius = self.diameter / 2

        self.sinkage = Constants.ROLLING_RESISTANCE_COEFFICIENT**2 / self.diameter # C_rr = sqrt(sinkage/diameter) (Google)
        self.rolling_radius = (self.radius - self.sinkage) / 3 # RoT (Motorcycle Dynamics - Vittore Cossalter)

