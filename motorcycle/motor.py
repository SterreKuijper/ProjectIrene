class Motor:
    def __init__(self, max_rpm, nominal_power, nominal_torque, max_power, max_torque, efficiency):
        self.max_rpm = max_rpm  # RPM
        self.nominal_power = nominal_power  # W
        self.nominal_torque = nominal_torque  # N
        self.max_power = max_power  # W
        self.max_torque = max_torque  # N
        self.efficiency = efficiency
