#!/usr/bin/env python3

"""
Generate all valid combinations of N pairs of parenthesis.

Completion time: 20 minutes.

Examples:
N == 1 -> ()
N == 2 -> ()(), (())
N == 3 -> ()()(), ((())), (()()), ()(()), (())()

Notes
- Did NOT notice that each step builds on the first part, but adding parens
  before, after and inside the previous one.
- Jumped directly to the build a string as you go, keeping track of open and
  close counts.
- Forgot the second loop where we generate the closure combos.
- Trickiness with the range +1 issue.
- Time is actually O(n!)
"""
from functools import lru_cache


@lru_cache()
def parens(n, to_close=0):
    # print('*')
    if n == 0:
        return {')'*to_close, }
    results = set()
    for i in range(1, n+1):
        for rest in parens(n-i, to_close+i):
            results.add('('*i + rest)
    for i in range(1, to_close+1):
        for rest in parens(n, to_close-i):
            results.add(')'*i + rest)
    return results


if __name__ == '__main__':
    print(parens(3))
    print(len(parens(4)))
    print(len(parens(5)))
    print(len(parens(10)))
