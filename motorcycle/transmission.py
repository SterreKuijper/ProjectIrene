class Transmission:
    def __init__(self, gear_ratios):
        self.gear_ratios = gear_ratios
        self.gears = len(self.gear_ratios * 2)

    def set_gear_ratios(self, gear_ratios):
        self.gear_ratios = gear_ratios
