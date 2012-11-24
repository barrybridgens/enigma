#
# Barry's Enigma simulator
#
# rotor.py
#
# A class to simulate Enigma rotors
#

from enigma_utility import *

# The rotor superclass
# All of the individual rotor classes inherit from this

class Rotor:

  def __init__(self):
    # The internal wiring of the rotor - determines which letter is translated to what
    self.wiring = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'    # default - will be changed for "real" rotors
    # The notch position where stepping this rotor will cause the "next" rotor to step
    self.notch_position = 20    # default - will be changed for "real" rotors
    # The ring setting - gives an offset from the "external" position to the actual wiring position
    self.ring_setting = 'A'

  def get_mapping(self, input_letter):
    wiring_position = letter_to_number(input_letter)
    wiring_position = (wiring_position + letter_to_number(self.ring_setting)) % 26
    return(self.wiring[wiring_position])

  def set_ring_setting(self, letter):
    self.ring_setting = letter
