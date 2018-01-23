def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    newdict = {}
    key = 0
    value = []
    for i in d:
        if d[i] != key:
            key = d[i]
            value = [i]
            value.sort()
            newdict[key] = value
        elif d[i] == key:
            value.append(i)
            value.sort()
            newdict[key] = value
    print(newdict)


d = {1: 10, 2: 20, 3: 30}
dict_invert(d)
d = {1: 10, 2: 20, 3: 30, 4: 30}
dict_invert(d)
d = {4: True, 2: True, 0: True}
dict_invert(d)
dict_invert({30000: 30, 600: 30, 2: 10})
