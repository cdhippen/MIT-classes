from fractions import Fraction

# formulas for lower and higher binding for bisectional search
monthlyInterestRate = Fraction(annualInterestRate / 12)
lower = Fraction(balance / 12)
higher = Fraction((balance * (1 + monthlyInterestRate) ** 12) / 12)

while True:
    guess = Fraction(((higher - lower) / 2 + lower))
    remaining = balance

    for i in range(12):
        unpaid = remaining - guess
        remaining = unpaid + monthlyInterestRate*unpaid

    if higher - lower <= Fraction(.01) and remaining < 0:
        result = round(float(lower), 2)
        print("Lowest Payment: %s" % result)
        break

    elif higher - lower <= Fraction(.01) and remaining >= 0:
        result = round(float(higher), 2)
        print("Lowest Payment: %s" % result)
        break

    elif remaining < Fraction(-0.01):
        higher = guess

    elif remaining > 0:
        lower = guess
