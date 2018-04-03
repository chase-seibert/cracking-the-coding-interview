#!/usr/bin/env python3

"""
Write a function to determine if a tic tac board has a winner.

Completion time: 15 minutes.

Examples:

Notes
- Just hard-code the win cases as tuples, can always generate them.
"""


def _get_positions(n):
    assert n == 3
    return [
        # rows
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        # cols
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        # diags
        ((0, 0), (1, 1), (2, 2)),
        ((2, 0), (1, 1), (0, 2)),
    ]


def has_won(b):
    for p1, p2, p3 in _get_positions(len(b[0])):
        (r1, c1), (r2, c2), (r3, c3) = p1, p2, p3
        v1, v2, v3 = b[r1][c1], b[r2][c2], b[r3][c3]
        if v1 == v2 == v3:
            return v1
    return None


if __name__ == '__main__':
    assert 'X' == has_won([
        ['X', 'O', None],
        ['X', 'X', 'O'],
        ['X', 'O', 'O'],
    ])
