def biggest(aDict):
    '''
    aDict: A dictionary, where all values are lists.
    returns: The key with the largest number of values associated with it.
    '''
    lengths = {}

    if len(aDict) >= 0:
        for i in aDict:
            lengths[str(i)] = len(aDict[i])
    else:
        return None
    return str(max(aDict, key=aDict.get))
