remaining = balance
for i in range(12):
    unpaid = remaining - monthlyPaymentRate * remaining
    remaining = round((unpaid + (annualInterestRate / 12) * unpaid), 2)
print('Remaining balance: %s' % remaining)
