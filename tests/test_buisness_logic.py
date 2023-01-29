import sys
from os.path import dirname, abspath

from pytest import approx, main, raises

test_directory = dirname(abspath(__file__))
project_directory = dirname(test_directory)
sys.path.append(project_directory)

from backend.constants import (
    MASS_NO_CHARGE_KG,
    MAX_TAKEOFF_TIME_SEC,
    TAKE_OFF_VELOCITY_MPS,
    ENGINES_FORCE_NEWTON,
    VELOCITY_0_MPS,
)

from backend.business_logic import (
    is_valid_charge_mass,
    calculate_acceleration,
    is_valid_charge_mass_string,
    minimal_acceleration,
    maximal_total_mass,
    maximal_charge_mass,
    calculate_takeoff_time,
    calculate_takeoff_distance,
    calculate_mass_to_destroy, ChargeMassErrorTooBig, InvalidChargeMass,
)


def test_minimal_acceleration():
    assert minimal_acceleration == TAKE_OFF_VELOCITY_MPS / MAX_TAKEOFF_TIME_SEC


def test_maximal_total_mass():
    assert maximal_total_mass == ENGINES_FORCE_NEWTON / minimal_acceleration


def test_maximal_charge_mass():
    assert maximal_charge_mass == maximal_total_mass - MASS_NO_CHARGE_KG


def test_is_valid_charge_mass():
    assert is_valid_charge_mass(0)
    assert is_valid_charge_mass(maximal_charge_mass)
    assert is_valid_charge_mass(1.11)
    assert not is_valid_charge_mass(-1)
    assert not is_valid_charge_mass("wbudwbwdb")
    with raises(TypeError):
        is_valid_charge_mass()


def test_is_valid_charge_mass_string():
    assert is_valid_charge_mass_string("0")
    assert is_valid_charge_mass_string("1.11")
    assert not is_valid_charge_mass_string("-1")
    # noinspection SpellCheckingInspection
    assert not is_valid_charge_mass_string("wbudwbwdb")
    with raises(TypeError):
        is_valid_charge_mass_string()


def test_calculate_acceleration():
    assert calculate_acceleration(0) == ENGINES_FORCE_NEWTON / MASS_NO_CHARGE_KG
    assert calculate_acceleration(maximal_charge_mass) == minimal_acceleration
    assert calculate_acceleration(1.11) == ENGINES_FORCE_NEWTON / (MASS_NO_CHARGE_KG + 1.11)
    with raises(InvalidChargeMass):
        calculate_acceleration(-1)
    with raises(ChargeMassErrorTooBig):
        calculate_acceleration(maximal_charge_mass + 1)


def test_calculate_takeoff_time():
    assert calculate_takeoff_time(0) == TAKE_OFF_VELOCITY_MPS / (ENGINES_FORCE_NEWTON / MASS_NO_CHARGE_KG)
    assert calculate_takeoff_time(maximal_charge_mass) == approx(MAX_TAKEOFF_TIME_SEC)
    with raises(InvalidChargeMass):
        calculate_takeoff_time(-1)
    with raises(ChargeMassErrorTooBig):
        calculate_takeoff_time(maximal_charge_mass + 1)


def test_calculate_takeoff_distance():
    acceleration_zero_mass = calculate_acceleration(0)
    take_off_time_zero_mass = calculate_takeoff_time(0)
    assert (calculate_takeoff_distance(0), (VELOCITY_0_MPS * take_off_time_zero_mass) + (
            acceleration_zero_mass * take_off_time_zero_mass ** 2) / 2)
    with raises(InvalidChargeMass):
        calculate_takeoff_distance(-1)
    with raises(ChargeMassErrorTooBig):
        calculate_takeoff_distance(maximal_charge_mass + 1)


def test_calculate_mass_to_destroy():
    assert calculate_mass_to_destroy(0) == 0
    with raises(InvalidChargeMass):
        calculate_mass_to_destroy(-1)
    assert calculate_mass_to_destroy(maximal_charge_mass) == 0
    assert calculate_mass_to_destroy(maximal_charge_mass + 1) == 1


if __name__ == '__main__':
    main()
