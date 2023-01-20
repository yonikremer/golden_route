import unittest

from constants import MASS_NO_CHARGE_KG, TAKE_OFF_VELOCITY_MPS, ENGINES_FORCE_NEWTON, VELOCITY_0_MPS
import business_logic


class MyTestCase(unittest.TestCase):
    def test_calculate_acceleration(self):
        self.assertEqual(business_logic.calculate_acceleration(0), ENGINES_FORCE_NEWTON / MASS_NO_CHARGE_KG)
        self.assertRaises(ValueError, business_logic.calculate_acceleration, -1)

    def test_calculate_takeoff_time(self):
        self.assertEqual(business_logic.calculate_takeoff_time(0),
                         TAKE_OFF_VELOCITY_MPS / (ENGINES_FORCE_NEWTON / MASS_NO_CHARGE_KG))
        self.assertRaises(ValueError, business_logic.calculate_takeoff_time, -1)
        self.assertRaises(ValueError, business_logic.calculate_takeoff_time, 1000000)

    def test_calculate_takeoff_distance(self):
        acceleration_zero_mass = business_logic.calculate_acceleration(0)
        take_off_time_zero_mass = business_logic.calculate_takeoff_time(0)
        self.assertEqual(business_logic.calculate_takeoff_distance(0),
                         (VELOCITY_0_MPS * take_off_time_zero_mass) + (acceleration_zero_mass * take_off_time_zero_mass ** 2) / 2)
        self.assertRaises(ValueError, business_logic.calculate_takeoff_distance, -1)
        self.assertRaises(ValueError, business_logic.calculate_takeoff_distance, 1000000)


if __name__ == '__main__':
    unittest.main()
