# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python

# todo: Доделать
def rot13(message):
    ret = ''
    for i in message:
        if i.isalpha():
            if i.isupper() and ord(i) + 13 > 90:
                ret += chr(65 + (13 - (90 - ord(i))))
            elif i.islower() and ord(i) + 13 > 122:
                ret += chr(97 + (13 - (122 - ord(i))))
            else:
                ret += (chr(ord(i) + 13))
        else:
            ret += i
    return ret