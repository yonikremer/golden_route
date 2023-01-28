import unittest

import business_logic
from constants import (
    ENGINES_FORCE_NEWTON,
    MASS_NO_CHARGE_KG,
    TAKE_OFF_VELOCITY_MPS,
    VELOCITY_0_MPS,
)


class MyTestCase(unittest.TestCase):

    def test_is_valid_charge_mass(self):
        self.assertTrue(business_logic.is_valid_charge_mass(0))
        self.assertTrue(
            business_logic.is_valid_charge_mass(
                business_logic.maximal_charge_mass))
        self.assertTrue(business_logic.is_valid_charge_mass(1.11))
        self.assertFalse(business_logic.is_valid_charge_mass(-1))
        self.assertFalse(business_logic.is_valid_charge_mass("wbudwbwdb"))
        self.assertRaises(TypeError, business_logic.is_valid_charge_mass)

    def test_is_valid_charge_mass_string(self):
        self.assertTrue(business_logic.is_valid_charge_mass_string("0"))
        self.assertTrue(business_logic.is_valid_charge_mass_string("1.11"))
        self.assertFalse(business_logic.is_valid_charge_mass_string("-1"))
        # noinspection SpellCheckingInspection
        self.assertFalse(
            business_logic.is_valid_charge_mass_string("wbudwbwdb"))
        self.assertRaises(TypeError, business_logic.is_valid_charge_mass)

    def test_calculate_acceleration(self):
        self.assertEqual(
            business_logic.calculate_acceleration(0),
            ENGINES_FORCE_NEWTON / MASS_NO_CHARGE_KG,
        )
        self.assertRaises(ValueError, business_logic.calculate_acceleration,
                          -1)

    def test_calculate_takeoff_time(self):
        self.assertEqual(
            business_logic.calculate_takeoff_time(0),
            TAKE_OFF_VELOCITY_MPS / (ENGINES_FORCE_NEWTON / MASS_NO_CHARGE_KG),
        )
        self.assertRaises(ValueError, business_logic.calculate_takeoff_time,
                          -1)
        self.assertRaises(ValueError, business_logic.calculate_takeoff_time,
                          1000000)

    def test_calculate_takeoff_distance(self):
        acceleration_zero_mass = business_logic.calculate_acceleration(0)
        take_off_time_zero_mass = business_logic.calculate_takeoff_time(0)
        self.assertEqual(
            business_logic.calculate_takeoff_distance(0),
            (VELOCITY_0_MPS * take_off_time_zero_mass) +
            (acceleration_zero_mass * take_off_time_zero_mass**2) / 2,
        )
        self.assertRaises(ValueError,
                          business_logic.calculate_takeoff_distance, -1)
        self.assertRaises(ValueError,
                          business_logic.calculate_takeoff_distance, 1000000)

    def test_calculate_mass_to_destroy(self):
        self.assertEqual(business_logic.calculate_mass_to_destroy(0), 0)
        self.assertRaises(ValueError, business_logic.calculate_mass_to_destroy,
                          -1)
        self.assertEqual(
            business_logic.calculate_mass_to_destroy(
                business_logic.maximal_charge_mass + 1),
            1,
        )


if __name__ == "__main__":
    unittest.main()
