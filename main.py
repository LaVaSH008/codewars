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
mov d 100
dec d
mov b d
jnz b -2
inc d
mov a d
jnz 5 10
mov c a
'''

    code1 = '''\
mov a 1
mov b 1
mov c 0
mov d 26
jnz c 2
jnz 1 5
mov c 7
inc d
dec c
jnz c -2
mov c a
inc a
dec b
jnz b -2
mov b c
dec d
jnz d -6
mov c 18
mov d 11
inc a
dec d
jnz d -2
dec c
jnz c -5
'''

    code3 = '''\
mov q 26
mov g 25
mov c 28
mov h 20
mov z 1
jnz z 4
jnz q 2
inc q
inc q
dec q
dec g
inc g
inc g
inc g
inc c
inc c
inc c
inc c
dec h
inc h
dec h
'''

    code4 = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''

    code5 = '''\
mov a 0
mov b 0
dec a
dec a
mov b a
jnz a -3
'''

    code = '''\
mov v 132 
mov e 0 
jnz e 3 
jnz v 2 
dec v 
dec e 
inc e 
inc v 
inc v
'''

    print(simple_assembler(code.splitlines()))
