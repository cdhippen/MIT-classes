import string

WORDLIST_FILENAME = 'words.txt'


# DO NOT MODIFY THIS FUNCTION
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


# DO NOT MODIFY THIS FUNCTION
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


class Message(object):
    # DO NOT MODIFY THIS METHOD
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    # DO NOT MODIFY THIS METHOD
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    # DO NOT MODIFY THIS METHOD
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
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

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        shift_text = ''
        for i in self.message_text:
            if i in shift_dict.keys():
                shift_text += shift_dict[i]
            else:
                shift_text += i
        return shift_text


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function
            load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        messages = {}
        words = self.message_text.split(' ')

        for i in range(26):
            msg_list = []
            message = ' '
            for x in words:
                self.message_text = x
                msg_list.append(self.apply_shift(i))
            message = message.join(msg_list)
            messages[i] = message

        values = []

        for y in range(len(words)):
            for x, i in messages.items():
                word_list = i.split(' ')
                if is_word(self.valid_words, word_list[y]):
                    values.append(x)

        shift = max(set(values), key=values.count)

        self.message_text = ' '.join(words)
        decrypt = self.apply_shift(shift)

        return shift, decrypt


test = CiphertextMessage('Stsxjsxj Btwix: Mjqqt, Btwqi!!')
print(test.decrypt_message())
