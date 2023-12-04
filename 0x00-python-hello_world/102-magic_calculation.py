#!/usr/bin/python3

#  3           0 LOAD_CONST               1 (98)
#            3 LOAD_FAST                0 (a)
#            6 LOAD_FAST                1 (b)
#            9 BINARY_POWER
#            10 BINARY_ADD
#            11 RETURN_VALUE

# corresponding function to the CPython bytecode

def magic_calculation(a, b):
    return 98 + (a ** b)
