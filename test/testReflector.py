# Test reflector

import unittest

from enigma import reflector
from enigma import enigma_utility

class TestReflector(unittest.TestCase):

    def setUp(self):
        self.reflector = reflector.Reflector()
        self.reflector_b = reflector.Reflector_B()
        self.reflector_c = reflector.Reflector_C()

    def tearDown(self):
        pass

    def test_reflector_class(self):
    	self.assertEqual(self.reflector.get_left_right_mapping('B'), 'Y')
    	self.assertEqual(self.reflector.get_left_right_mapping('F'), 'U')
    	self.assertEqual(self.reflector.get_left_right_mapping('Y'), 'B')
    	self.assertEqual(self.reflector.get_left_right_mapping('U'), 'F')

    def test_reflector_B_mapping(self):
        mapping = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        for num in range(0, 26):
            input_char = enigma_utility.number_to_letter(num)
            output_char = mapping[num]
            self.assertEqual(self.reflector_b.get_left_right_mapping(input_char), output_char)

    def test_reflector_C_mapping(self):
        mapping = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'
        for num in range(0, 26):
            input_char = enigma_utility.number_to_letter(num)
            output_char = mapping[num]
            self.assertEqual(self.reflector_c.get_left_right_mapping(input_char), output_char)