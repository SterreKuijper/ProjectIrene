from motorcycle.motorcycle import Motorcycle
from motorcycle.motor import Motor
from motorcycle.transmission import Transmission
from motorcycle.wheel import Wheel
from motorcycle.battery import Battery

# parts of the motorcycle
battery = Battery(voltage=126)

motor = Motor(
    max_rpm=6000,
    nominal_power=22,
    nominal_torque=50,
    max_power=40,
    max_torque=100,
    efficiency=0.92
)

rear_wheel = Wheel(
    width=150,
    aspect_ratio=0.6,
    rim_diameter_inch=17
)

front_wheel = Wheel(
    width=110,
    aspect_ratio=0.7,
    rim_diameter_inch=17
)

wheels = [rear_wheel, front_wheel]

transmission = Transmission(
    gear_ratios=[2.26, 1.66]
)

vortex = Motorcycle(
    transmission=transmission,
    battery=battery,
    motor=motor,
    wheels=wheels,
    mass=180,
    frontal_area=0.6,
    drag_coefficient=0.61,
    lift_coefficient=0.4
)
