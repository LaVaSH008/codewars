import math


def find_next_square(sq):
    return math.pow(math.sqrt(sq) + 1, 2) \
        if int(math.sqrt(sq)) == float(math.sqrt(sq)) \
        else -1
