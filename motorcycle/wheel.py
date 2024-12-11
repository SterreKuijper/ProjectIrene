import math
from utils.functions import inch_to_mm


class Wheel:

    def __init__(self, width, aspect_ratio, rim_diameter_inch):
        self.width = width
        self.aspect_ratio = aspect_ratio

        # Convert rim diameter from inches to mm
        self.rim_diameter_inch = rim_diameter_inch
        self.rim_diameter_mm = inch_to_mm(rim_diameter_inch)

        # Calculate crown radius (tire section height)
        self.crown_radius = width * aspect_ratio

        # Calculate overall diameter
        self.diameter = self.rim_diameter_mm + 2 * self.crown_radius

        # Calculate radius and circumference
        self.radius = self.diameter / 2
        self.circumference = self.diameter * math.pi
