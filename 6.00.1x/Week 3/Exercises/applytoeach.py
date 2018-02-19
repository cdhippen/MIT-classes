def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


testList = [1, -4, 8, -9]


def absval(i):
    return abs(i)


applyToEach(testList, absval)

print(testList)

testList = [1, -4, 8, -9]


def plusone(i):
    i += 1
    return i


applyToEach(testList, plusone)

print(testList)

testList = [1, -4, 8, -9]


def abssq(i):
    return abs(i**2)


applyToEach(testList, abssq)

print(testList)
