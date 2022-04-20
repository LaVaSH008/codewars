import re


def pig_it(text):
    c = []
    for i in re.findall(r'[0-9]+|[A-z]+|,| |"|!|\?', text):
        c.append(i + 'ay') if len(i) == 1 and not i in ', "!?' else None
        c.append(i) if i in ', "!?' else None
        c.append(i[1:-1] + i[-1] + i[0] + 'ay') if len(i) > 1 else None

    return ''.join(c)