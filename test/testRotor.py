# Test rotor

import unittest

from enigma import rotor
from enigma import enigma_utility

class TestRotor(unittest.TestCase):

    def setUp(self):
        self.rotor = rotor.Rotor()
        self.I_rotor = rotor.I_Rotor()
        self.II_rotor = rotor.II_Rotor()
        self.III_rotor = rotor.III_Rotor()
        self.IV_rotor = rotor.IV_Rotor()
        self.V_rotor = rotor.V_Rotor()

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

    def test_rotor_I_mapping(self):
        mapping = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        for num in range(0, 26):
            input_char = enigma_utility.number_to_letter(num)
            output_char = mapping[num]
            self.assertEqual(self.I_rotor.get_left_right_mapping(input_char), output_char)

    def test_rotor_II_mapping(self):
        mapping = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
        for num in range(0, 26):
            input_char = enigma_utility.number_to_letter(num)
            output_char = mapping[num]
            self.assertEqual(self.II_rotor.get_left_right_mapping(input_char), output_char)

    def test_rotor_III_mapping(self):
        mapping = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        for num in range(0, 26):
            input_char = enigma_utility.number_to_letter(num)
            output_char = mapping[num]
            self.assertEqual(self.III_rotor.get_left_right_mapping(input_char), output_char)

    def test_rotor_IV_mapping(self):
        mapping = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
        for num in range(0, 26):
            input_char = enigma_utility.number_to_letter(num)
            output_char = mapping[num]
            self.assertEqual(self.IV_rotor.get_left_right_mapping(input_char), output_char)

    def test_rotor_V_mapping(self):
        mapping = 'VZBRGITYUPSDNHLXAWMJQOFECK'
        for num in range(0, 26):
            input_char = enigma_utility.number_to_letter(num)
            output_char = mapping[num]
            self.assertEqual(self.V_rotor.get_left_right_mapping(input_char), output_char)

if __name__ == '__main__':
    unittest.main()
