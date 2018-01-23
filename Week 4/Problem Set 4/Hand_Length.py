def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    len_hand = 0
    for i in hand:
        len_hand += hand[i]
    return len_hand


hand = {'a': 1, 'h': 1, 'r': 1, 'e': 1, 'm': 2}
print(calculateHandlen(hand))
