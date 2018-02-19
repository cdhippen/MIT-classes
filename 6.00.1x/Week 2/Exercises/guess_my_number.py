high = 100
low = 0
guess = int((high - low) / 2 + low)

answer = ''

print('Please think of a number between 0 and 100!')

while answer != 'c':
    print('Is your secret number %s?' % (guess))
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' "
                   "to indicate the guess is too low. Enter "
                   "'c' to indicate I guessed correctly.")
    if answer == 'h':
        high = guess
        guess = int((high - low) / 2 + low)
    elif answer == 'l':
        low = guess
        guess = int(high - (high - low) / 2)
    elif answer == 'c':
        print("Game over. Your secret number was: %s" % (guess))
        break
    else:
        print('Sorry, I did not understand your input')
