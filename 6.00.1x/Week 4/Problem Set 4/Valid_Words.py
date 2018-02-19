def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    lword = word.lower()
    letters = {}
    for i in lword:
        letters[i] = letters.get(i, 0) + 1

    if word.upper() in wordList or lword in wordList or word in wordList:
        for i in letters:
            if i in hand:
                if hand[i] >= letters[i]:
                    continue
                else:
                    return False
            else:
                return False
        return True
    else:
        return False


word = 'rapture'
wordList = open('words.txt').read().split()
hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
