#
# Barry's Enigma simulator
#
# reflector.py
#
# A class to simulate Enigma reflectors
#

from enigma_utility import *

# The reflector superclass
# All of the individual reflector classes inherit from this

class Reflector:

  def __init__(self):
    # The internal wiring of the reflector - determines which letter is translated to what
    self.wiring = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'    # default - will be changed for "real" reflectors

  def get_left_right_mapping(self, input_letter):
    wiring_position = letter_to_number(input_letter)
    return(self.wiring[wiring_position])

  def get_right_left_mapping(self, input_letter):
    for x in range(0, 26):
      if (self.get_left_right_mapping(number_to_letter(x)) == input_letter):
        output_letter = number_to_letter(x)
    return(output_letter)


class Reflector_B(Reflector):

  def __init__(self):
    # The internal wiring of the reflector - determines which letter is translated to what
    self.wiring = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

class Reflector_C(Reflector):

  def __init__(self):
    # The internal wiring of the reflector - determines which letter is translated to what
    self.wiring = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'
