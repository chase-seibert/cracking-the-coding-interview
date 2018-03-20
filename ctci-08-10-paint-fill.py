#!/usr/bin/env python3

"""
Implement paint fill.

Completion time: 10 minutes.

Notes
- Recursive call up/down/left/right. No diagonals.
- Need to keep track of color you are replacing
- Problematic to use lru_cache because mutating matrix, unhashable, but matrix
  is it's own cache already. Tried manual caching, did not save anything.
- Cafeful of off by one/out of bounds with matrix + len(m)/len(m[0]), use
  row >= len(m), (usually row < len(m)). Off by on == use inclusive compare.
"""


def paint(m, color, row, col, old_color=None):
    if old_color is None:
        old_color = m[row][col]
    if row < 0 or row >= len(m):
        return m
    if col < 0 or col >= len(m[0]):
        return m
    if m[row][col] != old_color:
        return m
    m[row][col] = color
    for new_row, new_col in (
        (row+1, col),
        (row-1, col),
        (row, col+1),
        (row, col-1),
    ):
        paint(m, color, new_row, new_col, old_color)
    return m


def print_m(m):
    for row in m:
        print(''.join([str(c) for c in row]))
    print('='*len(m[0]))


if __name__ == '__main__':
    m = [
        [1, 1, 2, 1],
        [1, 1, 2, 2],
        [1, 2, 2, 3],
        [1, 1, 2, 3],
        [2, 3, 2, 2],
    ]
    print_m(m)
    paint(m, color=0, row=2, col=2)
    print_m(m)
