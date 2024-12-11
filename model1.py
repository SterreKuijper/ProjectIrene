from environment import Environment

class Model1:
    def __init__(self, motorcycle):
        self.motorcycle = motorcycle
        self.motorcycle.calculate_transmission_information()

        self.environment = Environment(
            amb_pressure=960,  # Pa
            amb_temperature_C=18
        )
        self.time_step = 0.01  # s
        self.speed_step = 1  # km/h

        mass_rider = 80  # kg
        self.total_mass = mass_rider + motorcycle.mass