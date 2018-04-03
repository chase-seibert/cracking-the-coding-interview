#!/usr/bin/env python3

"""
Swap two numbers w/o using a temp variable.

Completion time: 5 minutes.

Examples: 5, 3
a = a + b -> 8
b = a - b -> 5
a = a - b -> 3

Notes
- Knew it was subtraction.
- Other edge cases 0, -1, None.
- Trick: there is also an XOR solution, works for more data types.
"""


def swap(a, b):
    # return (b, a)
    a = a + b
    b = a - b
    a = a - b
    return a, b


if __name__ == '__main__':
    assert swap(5, 3) == (3, 5)
    assert swap(4, -1) == (-1, 4)
    assert swap(0, 1) == (1, 0)
