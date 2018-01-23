def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2
    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    result = 0
    while True:
        if b**result <= x:
            result += 1
            if b**result > x:
                result -= 1
                break
        else:
            break
    return result
