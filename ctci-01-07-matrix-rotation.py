#!/usr/bin/env python3

"""
Rotate a matrix in place by 90 degrees clockwise.

Completion time: ?? minutes. Never got it working.

Examples:

ABCD
EFGH
IJKL
MNOP

Notes
- Rotate four cells in one loop interation.
- Outer loop is columns 0 to ceil(len/2)
- Inner is rows
- Calculate length = n, layer, first, last, i = loop from first to last,
  offset, think about inner loop first, then top/left/bottom/right
- Write a function that does one layer, for easier testing
- Each of the 4 clauses has the previous right hand as the left hand
- Clauses are:
    m[first][i]
    m[last-offset][first]
    m[last][last-offset]
    m[i][last]
"""

import math


def rotate(m):
    n = len(m)
    for layer in range(int(n / 2.0)):
        _rotate_layer(m, layer, n)
    return m


def _rotate_layer(m, layer, n):
    first = layer
    last = n - layer - 1
    for i in range(first, last):
        offset = i - first
        temp = m[first][i]
        # top from left
        m[first][i] = m[last-offset][first]
        # left from bottom
        m[last-offset][first] = m[last][last-offset]
        # bottom from right
        m[last][last-offset] = m[i][last]
        # right from top
        m[i][last] = temp
    return m


def print_matrix(m):
    for row in m:
        print(''.join(row))
    print('---')


if __name__ == '__main__':
    m = [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H'],
        ['I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P'],
    ]
    print_matrix(m)
    m = rotate(m)
    # m = _rotate_layer(m, 1, 4)
    print_matrix(m)
