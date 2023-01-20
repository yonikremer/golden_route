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


def calculate_acceleration(charge_mass_kg):
    """Calculate the acceleration of the plane with a given charge mass."""
    if charge_mass_kg < 0:
        raise ValueError("The charge mass must non negative.")
    total_mass_kg = charge_mass_kg + MASS_NO_CHARGE_KG
    return ENGINES_FORCE_NEWTON / total_mass_kg


def calculate_takeoff_time(charge_mass_kg):
    """Calculate the time it takes to take off with a given charge mass.
    raises ValueError if the plane can't take off in MAX_TAKEOFF_TIME_SEC."""
    if charge_mass_kg < 0:
        raise ValueError("The charge mass must non negative.")
    acceleration_mps2 = calculate_acceleration(charge_mass_kg)
    takeoff_time_sec = TAKE_OFF_VELOCITY_MPS / acceleration_mps2
    if takeoff_time_sec > MAX_TAKEOFF_TIME_SEC:
        raise ValueError("The plane will not take off in time.")
    return takeoff_time_sec


def calculate_takeoff_distance(charge_mass_kg):
    """Calculate the distance it takes to take off with a given charge mass.
    raises ValueError if the plane can't take off in MAX_TAKEOFF_TIME_SEC."""
    if charge_mass_kg < 0:
        raise ValueError("The charge mass must non negative.")
    acceleration_mps2 = calculate_acceleration(charge_mass_kg)
    takeoff_time_sec = calculate_takeoff_time(charge_mass_kg)
    return (VELOCITY_0_MPS * takeoff_time_sec) + (acceleration_mps2 * takeoff_time_sec ** 2) / 2


def calculate_mass_to_destroy(charge_mass_kg):
    """Calculate the mass of the charge that will destroy the plane.
    raises ValueError if the plane can't take off in MAX_TAKEOFF_TIME_SEC."""
    if charge_mass_kg < 0:
        raise ValueError("The charge mass must non negative.")
    if charge_mass_kg <= maximal_charge_mass:
        # you don't need to destroy any charge
        return 0
    return charge_mass_kg - maximal_charge_mass


def main():
    charge_mass_kg = float(input("Enter the charge mass in kg: "))
    while charge_mass_kg < 0:
        print("The charge mass must be positive.")
        charge_mass_kg = float(input("Enter the charge mass in kg: "))

    try:
        takeoff_time_sec = calculate_takeoff_time(charge_mass_kg)
        print(f"The plane will take off in {takeoff_time_sec} seconds.")
        takeoff_distance_m = calculate_takeoff_distance(charge_mass_kg)
        print(f"The plane will take off {takeoff_distance_m} meters.")
    except ValueError:
        print("The plane will not take off in time.")
        print(f"In order to take off in time, you need to destroy"
              f" {calculate_mass_to_destroy(charge_mass_kg)} kg of charge.")


if __name__ == "__main__":
    main()
