from motorcycle.gear_stage import GearStage
from motorcycle.motorcycle import Motorcycle
from motorcycle.motor import Motor
from motorcycle.transmission import Transmission
from motorcycle.wheel import Wheel
from motorcycle.battery import Battery
from utils.constants import Constants

# parts of the motorcycle
battery = Battery(
    voltage=126, # V
    resistance=0.068 # ohm
)

motor = Motor(
    max_rpm=6000, # rpm
    nominal_power=22, # W
    nominal_torque=50, # N
    max_power=40, # W
    max_torque=100, # N
    efficiency=0.92
)

rear_wheel = Wheel(
    width=150,
    aspect_ratio=0.6,
    rim_diameter_inch=17
)

front_wheel = Wheel(
    width=110, # mm
    aspect_ratio=0.7,
    rim_diameter_inch=17 # inch
)

wheels = [rear_wheel, front_wheel]

first_gear_stage = GearStage(
    gear_ratio=2.53,
)

second_gear_stage = GearStage(
    gear_ratio=1.59,
)

gear_stages = [first_gear_stage, second_gear_stage]

transmission = Transmission(
    rear_chain_ratio=2.14,
    gear_stages= gear_stages,
    gear_efficiency=Constants.GEAR_EFFICIENCY
)

vortex = Motorcycle(
    transmission=transmission,
    battery=battery,
    motor=motor,
    wheels=wheels,
    wheelbase=1.38, # m
    mass=180, #kg
    frontal_area=0.6, # m^2
    drag_coefficient=0.61,
    lift_coefficient=0.4
)
