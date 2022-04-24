# https://www.codewars.com/kata/522551eee9abb932420004a0/train/python


def nth_fib(n):
    result = [0, 1]
    for i in range(2, n):
        result.append((result[i - 1]) + (result[i - 2]))
    return result[n - 1]
