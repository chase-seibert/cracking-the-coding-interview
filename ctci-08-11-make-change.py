#!/usr/bin/env python3

"""
Number of ways to make change for N cents with 25, 10, 5, 1 coins.

Completion time: 20 minutes.

Examples:
N == 11 -> 11p, 1n6p, 2n1p, 1d1p

Notes
- Decided to generate all options, and then count them.
- Realized that the recursive part was n-25, n-10, etc + other coin perms.
- Forgot base case of 1, needed to return a set of tuples NOT SET OF INTS
- Forgot order didn't matter, return a set of Counters. BUT Counter is not
hashable either, so use sorted tuple. Ex: tuple(sorted(coins))
- Tricks: sorted tuples for hashing, don't forget n==1 extra base case.
"""
from functools import lru_cache


@lru_cache()
def coin_perms(n):
    # print('*')
    if n <= 0:
        return set()
    if n == 1:
        # return a set OF TUPLES, not ints
        return {(1, ), }
    results = set()
    for coin in (25, 10, 5, 1):
        for coins in coin_perms(n-coin):
            results.add(tuple(sorted(coins + (coin, ))))
    return results


if __name__ == '__main__':
    print(coin_perms(11))
    print(len(coin_perms(100)))
