import string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remaining = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            remaining += i
    print(remaining)
    return remaining


getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
