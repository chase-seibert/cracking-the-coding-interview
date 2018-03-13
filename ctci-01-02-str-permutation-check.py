#!/usr/bin/env python3

"""
Given two strings, check if one is a permutation of the other.

Completion time: 14 minutes.

Assumptions: dupes OK, length matches.
Examples: ('abca', 'baac'), None, ''

Notes
- Check len() first for early exit optimization.
- Does == work for dicts?
- Would use a Counter in real life
- How to sort in python? -> sorted()
"""

from collections import Counter


def _char_counts(input_str):
    counts = {}
    for char in input_str:
        counts[char] = counts.get(char, 0) + 1
    return counts


def is_permutation(str1, str2):
    if str1 is None or str2 is None:
        return None
    if len(str1) != len(str2):
        return False
    return _char_counts(str1) == _char_counts(str2)


def is_permutation2(str1, str2):
    return Counter(str1) == Counter(str2)


if __name__ == '__main__':
    assert is_permutation('abca', 'baac')
    assert not is_permutation('abca', 'bac')
    assert not is_permutation('abca', 'babc')
    assert is_permutation2('abca', 'baac')
    assert not is_permutation2('abca', 'babc')
