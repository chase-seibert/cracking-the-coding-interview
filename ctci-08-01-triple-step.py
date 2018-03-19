#!/usr/bin/env python3

"""
Triple step, for n steps, if you can walk 1, 2 or 3 at a time, how many ways
are there to climb the steps?

Completion time: 20 minutes.

Examples: (1, 1), (2, 2), (3, 4), (4, ?)

Notes
- Right intution, f(n-1) + f(n-2) + f(n-3).
- Did not need as many base cases.
- Incorrectly simplified to 3 * f(n-1), but that does not account for the fact
  that for any new step, you are multipliying those possibilities by
  duplicating all the ways to get to n-3, then doing 3 steps, etc.
- Runtime is 3^n, but with memoization is O(n)
"""


from functools import lru_cache


@lru_cache()
def num_steps(n):
    base = {
        0: 0,
        1: 1,
        2: 2,
        3: 4,
    }
    if n in base:
        return base.get(n)
    return num_steps(n-1) + num_steps(n-2) + num_steps(n-3)


if __name__ == '__main__':
    assert num_steps(4) == 7
    print(num_steps(30))
