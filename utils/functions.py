from utils.constants import Constants


def inch_to_mm(value):
    return value * Constants.MM_PER_INCH


def mm_to_inch(value):
    return value / Constants.MM_PER_INCH


def celsius_to_kelvin(value):
    return value + Constants.KELVIN_CELSIUS_OFFSET


def kelvin_to_celsius(value):
    return value - Constants.KELVIN_CELSIUS_OFFSET


def rpm_to_rps(value):
    return value / 60


def rps_to_rpm(value):
    return value * 60


def ms_to_kmh(value):
    return value * 3.6


def kmh_to_ms(value):
    return value / 3.6
