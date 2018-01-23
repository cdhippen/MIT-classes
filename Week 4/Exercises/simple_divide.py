def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    try:
        return [simple_divide(item, denom) for item in list_of_numbers]
    except ZeroDivisionError:
        return [0 for item in list_of_numbers]


def simple_divide(item, denom):
    return item / denom
