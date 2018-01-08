def gcdIter(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    result = 0
    for i in range(a, 0, -1):
        if b % i == 0 and a % i == 0:
            result = i
            break
    return result
