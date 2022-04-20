import re


def valid_parentheses(string):
    s = re.findall(r'[\(-\)]', string)
    s1 = []

    for i in range(0, len(s)):
        if s[i] == ')':
            s1.append(s[i])
        elif s[i] == '(':
            try:
                s[s.index(')', i, len(s))] = ''
            except ValueError:
                s1.append(s[i])

    return True if len(s1) == 0 else False
