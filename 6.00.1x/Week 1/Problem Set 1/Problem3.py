s = 'azcbobobegghakl'
x = 'abcbcd'


def longer(s):
    perm = []
    for i in range(len(s)):
        count = 0
        count1 = 1
        temp = [s[i]]
        while i+count1 < len(s) and s[i+count] <= s[i+count1]:
            temp.append(s[i+count1])
            count += 1
            count1 += 1
        if len(temp) > len(perm):
            perm = temp[:]

    print(''.join(perm))


print(longer(s))
print(longer(x))
