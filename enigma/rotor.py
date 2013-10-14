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
    self.notch_position = 'N'    # default - will be changed for "real" rotors
    # The ring setting - gives an offset from the "external" position to the actual wiring position
    self.ring_setting = 'Z'

  def get_left_right_mapping(self, input_letter):
    wiring_position = letter_to_number(input_letter)
    wiring_position = (wiring_position + letter_to_number(self.ring_setting) + 1) % 26
    return(self.wiring[wiring_position])

  def get_right_left_mapping(self, input_letter):
    for x in range(0, 26):
      if (self.get_left_right_mapping(number_to_letter(x)) == input_letter):
        output_letter = number_to_letter(x)
    return(output_letter)


  def set_ring_setting(self, letter):
    self.ring_setting = letter

  def is_notch(self, rotor_position):
    return(self.notch_position == rotor_position)



class I_Rotor(Rotor):

  def __init__(self):
    Rotor.__init__(self)
    # The internal wiring of the rotor - determines which letter is translated to what
    self.wiring = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
    # The notch position where stepping this rotor will cause the "next" rotor to step
    self.notch_position = 'Q'    

class II_Rotor(Rotor):

  def __init__(self):
    Rotor.__init__(self)
    # The internal wiring of the rotor - determines which letter is translated to what
    self.wiring = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
    # The notch position where stepping this rotor will cause the "next" rotor to step
    self.notch_position = 'E' 

class III_Rotor(Rotor):

  def __init__(self):
    Rotor.__init__(self)
    # The internal wiring of the rotor - determines which letter is translated to what
    self.wiring = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
    # The notch position where stepping this rotor will cause the "next" rotor to step
    self.notch_position = 'V' 

class IV_Rotor(Rotor):

  def __init__(self):
    Rotor.__init__(self)
    # The internal wiring of the rotor - determines which letter is translated to what
    self.wiring = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
    # The notch position where stepping this rotor will cause the "next" rotor to step
    self.notch_position = 'J' 

class V_Rotor(Rotor):

  def __init__(self):
    Rotor.__init__(self)
    # The internal wiring of the rotor - determines which letter is translated to what
    self.wiring = 'VZBRGITYUPSDNHLXAWMJQOFECK'
    # The notch position where stepping this rotor will cause the "next" rotor to step
    self.notch_position = 'Z' 