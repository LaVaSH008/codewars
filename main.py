from methods.kuy5.rgb import rgb
from methods.kuy5.simple_assembler import simple_assembler
from methods.kuy5.validParentheses import valid_parentheses
from methods.kyu7.find_next_square import find_next_square
from methods.kyu6.spin_words import spin_words
from methods.kuy5.move_zeros import move_zeros
from methods.kyu7.binary_array_to_number import binary_array_to_number
from methods.kyu4.range_extraction import solution
from methods.kyu4.snail import snail
from methods.kyu7.square_digits import square_digits

if __name__ == '__main__':
    code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''
    print(simple_assembler(code))
