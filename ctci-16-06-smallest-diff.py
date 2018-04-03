#!/usr/bin/env python3

"""
Compute smallest diff between any pair in two unsorted lists of integers.

Completion time: 15 minutes.

Examples: [1, 4, 10], [-1, 5, 12] -> (4, 5) == 1

Notes
- Got brute force right away, O(n*m).
- Jumped to sort both, then binary search one.
- Can actually just sort one of them (smaller).
"""
import bisect
import sys


def smallest_diff(a, b):
    a = sorted(a)
    min_pair, diff = None, sys.maxsize
    for val in b:
        i = bisect.bisect_left(a, val)
        for j in (i-1, i, i+1):
            if 0 <= j < len(a):
                if abs(a[j] - val) < diff:
                    min_pair = (a[j], val)
                    diff = abs(a[j] - val)
    return min_pair, diff


if __name__ == '__main__':
    print(smallest_diff([1, 4, 10], [-1, 5, 12]))
