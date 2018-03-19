#!/usr/bin/env python3

"""
Given a set S, generate all subsets.

Completion time: 20 minutes.

Examples: set(1, 2, 3) -> 1,2,3 1,2 1,3 1 2,3 2 3

Notes
- Realized right away I could represent all subsets in binary.
- Got right time: O(2^n)
- Wrong base case (combined len 0 and 1 case), 1 case is TWO subsets.
- Sets and tuples can be hard to use, try lists. At least, don't try
  sets of sets!
- For sets, use .add()
"""
import math

def subsets(s):
    if len(s) == 0:
        return {}
    if len(s) == 1:
        return {(), (s[0], )}
    first, rest = s[0], s[1:]
    results = set()
    for subset in subsets(rest):
        results.add((first, ) + subset)
        results.add(subset)
    return results


if __name__ == '__main__':
    print(subsets((3, 2, 1)))
