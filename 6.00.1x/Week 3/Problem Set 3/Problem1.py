def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord
    are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i in lettersGuessed:
            continue
        else:
            return False
            break
    return True


isWordGuessed('apple', ['e', 'i', 'k', 'p', 'r', 's'])
