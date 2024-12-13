class Motorcycle:

    def __init__(self, transmission, battery, motor, rear_wheel, front_wheel, wheelbase, mass, frontal_area, drag_coefficient, lift_coefficient):
        self.transmission = transmission
        self.battery = battery
        self.motor = motor
        self.rear_wheel = rear_wheel
        self.front_wheel = front_wheel
        self.wheelbase = wheelbase
        self.mass = mass
        self.frontal_area = frontal_area
        self.drag_coefficient = drag_coefficient
        self.lift_coefficient = lift_coefficient
        self.calculate_transmission_information()

    def calculate_transmission_information(self):
        self.transmission.calculate_gear_stages_information(self.motor, self.rear_wheel)
