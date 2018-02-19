bob = 'bob'
count = 0
bob_len = len(bob)

for i in range(len(s)):
    if s[i:i+bob_len] == bob:
        count += 1

print(count)
