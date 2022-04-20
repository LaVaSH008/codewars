def rgb(r, g, b):
    l = ''
    for i in [r, g, b]:
        i = 255 if i > 255 else i
        i = 0 if i < 0 else i
        l += r'{:02X}'.format(i)
    return l