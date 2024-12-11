from utils.functions import rpm_to_rps
from utils.functions import ms_to_kmh

class Transmission:
    def __init__(self, rear_chain_ratio, gear_stages, gear_efficiency):
        self.rear_chain_ratio = rear_chain_ratio
        self.gear_stages = gear_stages
        self.gear_efficiency = gear_efficiency
        self.active_gear_stage = gear_stages[0]

    def calculate_gear_stages_information(self, motor, wheel):
        for gear_stage in self.gear_stages:
            gear_stage.calculate_total_ratio(self.rear_chain_ratio)

            motor_max_rps = rpm_to_rps(motor.max_rpm)
            top_speed_ms = motor_max_rps * wheel.circumference / gear_stage.gear_ratio
            top_speed_kmh = ms_to_kmh(top_speed_ms)

            gear_stage.set_top_speed(top_speed_kmh)
            gear_stage.set_nominal_torque(motor.nominal_torque * gear_stage.gear_ratio.gear_ratio)
            gear_stage.set_max_torque(motor.max_torque * gear_stage.gear_ratio)

