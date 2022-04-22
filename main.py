from methods.kuy5.score import score
from methods.kuy5.simple_assembler import simple_assembler
from methods.kuy5.validParentheses import valid_parentheses
from methods.kyu7.find_next_square import find_next_square
from methods.kyu6.spin_words import spin_words
from methods.kuy5.move_zeros import move_zeros
from methods.kyu7.binary_array_to_number import binary_array_to_number
from methods.kyu4.range_extraction import solution

if __name__ == '__main__':
    code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''

    print(simple_assembler(code.splitlines()))
