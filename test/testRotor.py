# Test task

import unittest

from enigma import rotor
from enigma import enigma_utility

class TestRotor(unittest.TestCase):

    def setUp(self):
        self.rotor = rotor.Rotor()

    def tearDown(self):
        pass

# Tests for the rotor base class
    def test_rotor_class_mapping(self):
        self.assertEqual(self.rotor.get_left_right_mapping('B'), 'Y')
        self.assertEqual(self.rotor.get_left_right_mapping('X'), 'C')
        self.assertEqual(self.rotor.get_right_left_mapping('T'), 'G')
        self.assertEqual(self.rotor.get_right_left_mapping('O'), 'L')
        self.rotor.set_ring_setting('B')
        self.assertEqual(self.rotor.get_left_right_mapping('B'), 'W')
        self.assertEqual(self.rotor.get_left_right_mapping('Z'), 'Y')
        self.assertEqual(self.rotor.get_right_left_mapping('T'), 'E')
        self.assertEqual(self.rotor.get_right_left_mapping('O'), 'J')

    def test_rotor_class_notch_position(self):
        for num in range(0, 26):
            if (enigma_utility.number_to_letter(num) == 'N'):
                self.assertTrue(self.rotor.is_notch(enigma_utility.number_to_letter(num)))
            else:
                self.assertFalse(self.rotor.is_notch(enigma_utility.number_to_letter(num)))


if __name__ == '__main__':
    unittest.main()
