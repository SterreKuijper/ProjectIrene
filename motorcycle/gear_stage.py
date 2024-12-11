class GearStage:
    def __init__(self, gear_ratio):
        self.gear_ratio = gear_ratio
        self.total_ratio = None
        self.top_speed = None
        self.nominal_torque = None
        self.max_torque = None

    def calculate_total_ratio(self, rear_chain_ratio):
        self.total_ratio = rear_chain_ratio * self.gear_ratio

    def set_top_speed(self, value):
        self.top_speed = value

    def set_nominal_torque(self, value):
        self.nominal_torque = value

    def set_max_torque(self, value):
        self.max_torque = value
