import string


def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
    ascii_list = list(string.ascii_lowercase)
    ascii_list1 = list(string.ascii_uppercase)
    shifted_dict = {}

    for idx, val in enumerate(ascii_list):
        shifted_dict[val] = ascii_list[(idx+shift) % len(ascii_list)]
    for idx, val in enumerate(ascii_list1):
        shifted_dict[val] = ascii_list1[(idx+shift) % len(ascii_list1)]

    return shifted_dict


def apply_shift(text, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = build_shift_dict(shift)
        shift_text = ''
        for i in text:
            if i in shift_dict.keys():
                shift_text += shift_dict[i]
            else:
                shift_text += i
        return shift_text


apply_shift('Hello, world!', 5)
