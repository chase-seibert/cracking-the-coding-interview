#!/usr/bin/env python3

"""
Zero out any columns and rows in a NxM matrix that contain a zero.

Completion time: 20 minutes.

Examples:

A0B  => 000
CDE     C0E

Notes
- Careful not to zero out based on zeros you already replaced.
- Two passes, first time create sets of rows/cols to zero out.
"""


def zero_out(m):
    if not m:
        return m
    rows_to_zero, cols_to_zero = set(), set()
    num_rows, num_cols = len(m), len(m[0])
    for row in range(num_rows):
        for col in range(num_cols):
            if m[row][col] == 0:
                rows_to_zero.add(row)
                cols_to_zero.add(col)
    if not rows_to_zero or not cols_to_zero:
        return m
    for row in range(num_rows):
        for col in range(num_cols):
            if row in rows_to_zero or col in cols_to_zero:
                m[row][col] = 0
    return m


def print_matrix(m):
    for row in m:
        print(''.join([str(c) for c in row]))


if __name__ == '__main__':
    m = [
        ['A', 0, 'B'],
        ['C', 'D', 'E']
    ]
    zero_out(m)
    print_matrix(m)
