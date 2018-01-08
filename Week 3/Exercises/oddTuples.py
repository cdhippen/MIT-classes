def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    a = ()
    for i in range(0, len(aTup), 2):
        a += (aTup[i],)
    return a
