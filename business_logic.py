from numbers import Real
from typing import Callable

from constants import (
    MASS_NO_CHARGE_KG,
    MAX_TAKEOFF_TIME_SEC,
    TAKE_OFF_VELOCITY_MPS,
    ENGINES_FORCE_NEWTON,
    VELOCITY_0_MPS
)


minimal_acceleration = TAKE_OFF_VELOCITY_MPS / MAX_TAKEOFF_TIME_SEC
maximal_total_mass = ENGINES_FORCE_NEWTON / minimal_acceleration
maximal_charge_mass = maximal_total_mass - MASS_NO_CHARGE_KG


class ChargeMassErrorTooBig(ValueError):
    pass


def is_valid_charge_mass(charge_mass_kg) -> bool:
    """Check if the charge mass is valid."""
    return isinstance(charge_mass_kg, Real) and charge_mass_kg >= 0


def is_valid_charge_mass_string(charge_mass_kg_str: str) -> bool:
    """Check if the charge mass is valid."""
    try:
        charge_mass_kg = float(charge_mass_kg_str)
    except ValueError:
        return False
    return is_valid_charge_mass(charge_mass_kg)


def check_charge_mass_input(func: Callable):
    """Check if the charge mass is valid."""
    def wrapper(*args, **kwargs):
        charge_mass_kg = kwargs["charge_mass_kg"] if "charge_mass_kg" in kwargs else args[0]
        if not is_valid_charge_mass(charge_mass_kg):
            raise ValueError("The charge mass must be a non-negative number.")
        return func(*args, **kwargs)
    return wrapper


@check_charge_mass_input
def calculate_acceleration(charge_mass_kg: Real) -> Real:
    """Calculate the acceleration of the plane with a given charge mass."""
    total_mass_kg = charge_mass_kg + MASS_NO_CHARGE_KG
    return ENGINES_FORCE_NEWTON / total_mass_kg


@check_charge_mass_input
def calculate_takeoff_time(charge_mass_kg: Real) -> Real:
    """Calculate the time it takes to take off with a given charge mass.
    raises ValueError if the plane can't take off in MAX_TAKEOFF_TIME_SEC."""
    acceleration_mps2 = calculate_acceleration(charge_mass_kg)
    takeoff_time_sec = TAKE_OFF_VELOCITY_MPS / acceleration_mps2
    if takeoff_time_sec > MAX_TAKEOFF_TIME_SEC:
        raise ChargeMassErrorTooBig("The plane will not take off in time.")
    return takeoff_time_sec


@check_charge_mass_input
def calculate_takeoff_distance(charge_mass_kg: Real) -> Real:
    """Calculate the distance it takes to take off with a given charge mass.
    raises ValueError if the plane can't take off in MAX_TAKEOFF_TIME_SEC."""
    acceleration_mps2 = calculate_acceleration(charge_mass_kg)
    takeoff_time_sec = calculate_takeoff_time(charge_mass_kg)
    return (VELOCITY_0_MPS * takeoff_time_sec) + (acceleration_mps2 * takeoff_time_sec ** 2) / 2


@check_charge_mass_input
def calculate_mass_to_destroy(charge_mass_kg: Real) -> Real:
    """Calculate the mass of the charge that will destroy the plane.
    raises ValueError if the plane can't take off in MAX_TAKEOFF_TIME_SEC."""
    if charge_mass_kg <= maximal_charge_mass:
        # you don't need to destroy any charge
        return 0
    return charge_mass_kg - maximal_charge_mass


def main():
    charge_mass_kg_str = input("Enter the charge mass in kg: ")
    while not is_valid_charge_mass_string(charge_mass_kg_str):
        print("The charge mass must be positive.")
        charge_mass_kg_str = input("Enter the charge mass in kg: ")

    charge_mass_kg = float(charge_mass_kg_str)

    try:
        takeoff_time_sec = calculate_takeoff_time(charge_mass_kg)
        print(f"The plane will take off in {takeoff_time_sec} seconds.")
        takeoff_distance_m = calculate_takeoff_distance(charge_mass_kg)
        print(f"The plane will take off {takeoff_distance_m} meters.")
    except ChargeMassErrorTooBig:
        print("The plane will not take off in time.")
        print(f"In order to take off in time, you need to destroy"
              f" {calculate_mass_to_destroy(charge_mass_kg)} kg of charge.")


if __name__ == "__main__":
    main()
