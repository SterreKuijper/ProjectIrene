from utils.constants import Constants


def inch_to_mm(value):
    return value * Constants.MM_PER_INCH


def mm_to_inch(value):
    return value / Constants.MM_PER_INCH


def celsius_to_kelvin(value):
    return value + 273


def kelvin_to_celsius(value):
    return value - 273
