#!/usr/bin/env python3

"""
Given a sorted array with no dupes, find an i where a[i] == i.
Follow up: there ARE dupes

Completion time: 25 minutes.

Examples: -1, 0, 2, 3, 5, 6, 7
           0, 1, 2, 3, 4, 5, 6 <- index

Notes
- Brute force would work, but could also binary search in log(n).
- Slicing makes the problem more complicated, use start/end.
- For binary search, do +/- 1 on the recursive call, AND ending condition
  should be end < start.
"""


def magic_index(a, start=0, end=None):
    end = end or len(a) - 1
    mid = int((start + end) / 2)
    val = a[mid]
    i = mid
    # print(a, start, end, val)
    if end < start:
        return None
    if val == i:
        return i
    if val > i:
        return magic_index(a, start, mid-1)
    return magic_index(a, mid+1, end)


if __name__ == '__main__':
    assert magic_index([-1, 0, 2, 3, 5, 6, 7]) == 3
    assert magic_index([-1, 0, 2, 4, 5, 6, 7]) == 2
    assert magic_index([-1, -1, -1, -1, -1, -1, -1]) is None
