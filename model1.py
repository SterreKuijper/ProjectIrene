from environment import Environment


class Model1:
    def __init__(self, motorcycle):
        self.motorcycle = motorcycle
        self.mass_rider = 80  # kg
        self.environment = Environment(
            amb_pressure=960,  # Pa
            amb_temperature_C=18
        )
        self.time_step = 0.01  # s
        self.speed_step = 1  # km/h

    def get_max_something(self):
        max_something = 0
        return max_something

    def get_motor_transmission_gear_ratios(self):
        return self.motorcycle.transmission.gear_ratios
