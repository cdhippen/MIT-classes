def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        combo = []
        combo1 = []
        for j in range(N):
            # test bit jth of integer i
            if (i // 3**j) % 3 == 1:
                combo.append(items[j])
            if (i // 3**j) % 3 == 0:
                combo1.append(items[j])
        yield (combo, combo1)


for i in powerSet(['a', 'b', 'c']):
    print(i)
