def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        result = 1
    else:
        if exp == 1:
            result = base
        else:
            result = base * recurPower(base, exp - 1)
    return result
