def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for i in secretWord:
        if i in lettersGuessed:
            result += i
        elif i not in lettersGuessed:
            result += '_'
    return result


getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])
