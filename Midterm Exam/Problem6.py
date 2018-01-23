def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    smaller = min([a, b])
    list_of_divisors = []
    for i in range(1, smaller):
        if b % i == 0 and a % i == 0:
            list_of_divisors.append(i)
    results = list_of_divisors[::-1]
    if a == 1 or b == 1:
        result = 1
    elif a == 0 or b == 0:
        result = 0
    else:
        result = results[0]
    print(result)
    return result


gcd(134634125, 12341235)
gcd(0, 25)
gcd(1, 1)
gcd(25, 1)


def gcd2(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if b == 0:
        result = a
    else:
        result = gcd2(b, a % b)
    return result


gcd2(134634125, 12341235)
