#!/usr/bin/env python3

"""
Merge two sorted arrays A and B, given that A has a buffer at the end of len B.

Completion time: 25 minutes.

Examples:
A -> [1, 3, 5, None, None, None]
B -> [2, 4, 6]

Notes
- Find index where you should start merging.
- Copy rest of A. Iterate keeping separate indexes for B, A'.
- Simpler would be to just create the new array on the fly.
- Can do this without copying the sub-array if you start at the end.
"""


def merge(a, b):
    if len(b) > len(a):
        a, b = b, a
    for ai in range(len(a)):
        if b[0] > a[ai]:
            break
    c = a[ai:]
    bi, ci = 0, 0
    for ai in range(ai, len(a)):
        if c[ci] is None or b[bi] < c[ci]:
            a[ai] = b[bi]
            bi += 1
        else:
            a[ai] = c[ci]
            ci += 1
    return a


def merge_back(a, b):
    if len(b) > len(a):
        a, b = b, a
    ai, bi = len(a) - len(b) - 1, len(b) - 1
    for end in range(len(a) - 1, 0, -1):
        if a[ai] > b[bi]:
            a[end] = a[ai]
            ai -= 1
        else:
            a[end] = b[bi]
            bi -= 1
    return a


if __name__ == '__main__':
    a = [1, 3, 5, None, None, None]
    b = [2, 4, 6]
    print(merge_back(a, b))
