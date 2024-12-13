import sympy as sp

from vortex import vortex
from model1 import Model1
from utils.constants import Constants

# Define model
model = Model1(vortex)

# Define symbols
F_drive, F_drag, F_lift = sp.symbols('F_drive F_drag F_lift')
F_roll_res_front, F_roll_res_rear = sp.symbols('F_roll_res_front F_roll_res_rear')
F_friction_front, F_friction_rear = sp.symbols('F_friction_front F_friction_rear')
F_normal_front, F_normal_rear = sp.symbols('F_normal_front F_normal_rear')
a_x, m, g, v = sp.symbols('a_x m g v')  # Acceleration, mass, gravity, velocity
A, T_motor, r_wheel = sp.symbols('A T_motor r_wheel')  # Frontal area, torque and wheel radius,
C_d, C_l, C_rr, mu_s, rho_air = sp.symbols('C_d C_l C_rr mu_s rho_air')  # Constants: drag, lift, rolling resistance, static friction, air density

# Geometry dimensions
wheelbase = model.motorcycle.wheelbase  # m
CoM_base = 0.45*wheelbase  # m (distance from rear wheel to CoM along the base)
CoM_height = 0.45*wheelbase  # m RoT: h/p ~ 0.3-0.45 (Motorcycle Dynamics - Vittore Cossalter)
CoP_base = 0.55*wheelbase  # m (distance from rear wheel to CoP along the base)
CoP_height = 0.5*wheelbase  # m

# Constants for forces
gravitational_acceleration = Constants.GRAVITATIONAL_ACCELERATION  # m/s^2
rolling_resistance_coefficient = Constants.ROLLING_RESISTANCE_COEFFICIENT
drag_coefficient = Constants.DRAG_COEFFICIENT
lift_coefficient = Constants.LIFT_COEFFICIENT
frontal_area = model.motorcycle.frontal_area  # m^2
mass_body = model.total_mass  # kg
wheel_rolling_radius = model.motorcycle.rear_wheel.rolling_radius  # m (same radius for both wheels)
air_density = model.environment.air_density  # kg/m^3

""" Steady State Rectilinear Motion"""

# Drag force
F_drag_eq = sp.Eq(F_drag, 0.5 * air_density * C_d * A * v**2)

# Lift force (reduces normal force)
F_lift_eq = sp.Eq(F_lift, 0.5 * air_density * C_l * A * v**2)

# Rolling resistance on each wheel
F_roll_front_eq = sp.Eq(F_roll_res_front, C_rr * F_normal_front)
F_roll_rear_eq = sp.Eq(F_roll_res_rear, C_rr * F_normal_rear)

# Driving force from torque
F_drive_eq = sp.Eq(F_drive, T_motor / r_wheel)

# Force balance in x-direction
force_x_eq = sp.Eq(F_drive - F_drag - F_roll_res_front - F_roll_res_rear, m * a_x)

# Force balance in y-direction
force_y_eq = sp.Eq(F_normal_front + F_normal_rear - m * g + F_lift, 0)

# Moment balance about rear wheel
moment_eq = sp.Eq(
    # Moments due to forces (force * perpendicular distance to rear wheel)
    F_normal_front * wheelbase
    - F_drag * CoP_height
    - F_lift * CoP_base
    - m * g * CoM_base
    + F_drive * CoM_height,
    0,
)

# Substitutions
substitutions = {
    m: mass_body,
    g: gravitational_acceleration,
    C_d: drag_coefficient,
    C_l: lift_coefficient,
    A: frontal_area,
    air_density: air_density,
    C_rr: rolling_resistance_coefficient,
    r_wheel: wheel_rolling_radius,
    T_motor: 188,  # Example motor torque in Nm (Transmission_Calculation)
    a_x: 4.88,  # Example x-acceleration in m/s^2 (Transmission_Calculation)
    v: 0,  # Example velocity in m/s
}

# Solve the system of equations for unknowns: F_normal_front, F_normal_rear
force_system = [
    F_drag_eq.subs(substitutions),
    F_lift_eq.subs(substitutions),
    F_roll_front_eq.subs(substitutions),
    F_roll_rear_eq.subs(substitutions),
    F_drive_eq.subs(substitutions),
    force_x_eq.subs(substitutions),
    force_y_eq.subs(substitutions),
    moment_eq.subs(substitutions),
]

unknowns = [F_normal_front, F_normal_rear]
solutions = sp.solve(force_system, unknowns)

# Display results
for var, val in solutions.items():
    print(f"{var} = {val:.2f} N")