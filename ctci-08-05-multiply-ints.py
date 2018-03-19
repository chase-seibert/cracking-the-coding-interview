#!/usr/bin/env python3

"""
Multiple two ints without using multiplication.

Completion time: 30 minutes.

Examples: 3x5 = 5 + 5 + 5

Notes
- Tried addition first. Worked, but was slower.
- Had to use recursion, refactored.
- Hint was tried to count half and double it.
"""


def multiply(a, b):
    if a > b:
        a, b = b, a
    if a == 1:
        return b
    return b + multiply(a-1, b)


def mult2(a, b):
    if a > b:
        a, b = b, a
    if a == 1:
        return b
    first_half = mult2(a, int(b/2))
    if b % 2 == 0:
        return first_half + first_half
    second_half = mult2(a, b - int(b/2))
    return first_half + second_half


if __name__ == '__main__':
    assert multiply(3, 5) == 15
    assert multiply(100, 5) == 500
    assert mult2(100, 5) == 500
