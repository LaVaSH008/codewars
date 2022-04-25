# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python


def rot13(message):
    ret = ''
    for i in message:
        if i.isalpha():
            if 90 >= ord(i) > 77 or 122 >= ord(i) > 109:
                ret += chr(-13 + ord(i))
            else:
                ret += chr(13 + ord(i))
        else:
            ret += i
    return ret