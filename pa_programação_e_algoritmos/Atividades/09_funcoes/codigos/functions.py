def add(var1, var2):
    sum = var1 + var2
    return sum


def find_concept(var):
    if var >= 9:
        result = 1
    elif var >= 7.5:
        result = 2
    elif var >= 6:
        result = 3
    elif var >= 4:
        result = 4
    else:
        result = 5
    return result


def find_max(var):
    biggest = var[0]
    for i in var[1:]:
        if i > biggest:
            biggest = i
    return biggest
