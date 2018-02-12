def genPrimes():
    x = 1
    primes = []
    while True:
        x += 1
        if x not in primes:
            for i in range(2, x):
                if x % i == 0:
                    break
            else:
                primes.append(x)
                yield x
