#
# Barry's Enigma simulator
#
# enigma_utility.py
#
# Various usefull functions
#

def letter_to_number(letter):
    return(ord(letter) - ord('A'))

def number_to_letter(number):
    return(chr(number + ord('A')))
