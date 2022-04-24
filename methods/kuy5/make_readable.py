# https://www.codewars.com/kata/52685f7382004e774f0001f7/solutions/python


def make_readable(seconds):
    return ':'.join([str(r'{:02}'.format(seconds // 3600)),
                     r'{:02}'.format(int(seconds / 60) % 60),
                     r'{:02}'.format(seconds % 60)])
