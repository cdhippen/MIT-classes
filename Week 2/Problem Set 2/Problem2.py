def remaining(pay):
    air = annualInterestRate
    remaining = balance
    for d in range(12):
        unpaid = remaining - pay
        remaining = unpaid + (air / 12) * unpaid
    return remaining


for i in range(0, balance, 10):
    if remaining(i) < 0:
        print(i)
        break
