# -*- coding: utf-8 -*-

def mult(*digits):
    result = 1
    for d in digits:
        result *= d
    return result

print(mult(10, 20 ,30, 40))

def print_dict(**kwargs):
    for item in kwargs.items():
        print(*item, sep=": ")

print_dict(last_name='Ivan', first_name='Petrov')