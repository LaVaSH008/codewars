def move_zeros(array):
    return list(filter(lambda a: a != 0, array)) + [0]*array.count(0)
