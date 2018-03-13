#!/usr/bin/env python3

"""
Given a string, is it a permutation of a palindrome?

Completion time: 10 minutes.

Examples: "aabbc" -> True ("abcba")
Other palindromes: "abba", "aaaa", "aaa"

Notes
- Notice that all palindromes have 0 or 1 characters with a odd frequency.
- Generator statements don't have a length, use list comprehension.
"""


from collections import Counter


def can_be_palindrome(input_str):
    counts = Counter(input_str)
    return len([v for v in counts.values() if v % 2 == 1]) <= 1


if __name__ == '__main__':
    assert can_be_palindrome('aabbc')
    assert can_be_palindrome('baba')
    assert can_be_palindrome('aaaa')
    assert can_be_palindrome('aaacc')
    assert can_be_palindrome('aaccd')
