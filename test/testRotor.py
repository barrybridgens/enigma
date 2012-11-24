# Test task

import unittest

from enigma import rotor

class TestRotor(unittest.TestCase):

    def setUp(self):
        self.rotor = rotor.Rotor()

    def tearDown(self):
        pass

    def test_rotor_class(self):
        self.assertEqual(self.rotor.get_mapping('A'), 'Z')
        self.assertEqual(self.rotor.get_mapping('Z'), 'A')
        self.rotor.set_ring_setting('B')
        self.assertEqual(self.rotor.get_mapping('A'), 'Y')
        self.assertEqual(self.rotor.get_mapping('Z'), 'Z')


if __name__ == '__main__':
    unittest.main()
