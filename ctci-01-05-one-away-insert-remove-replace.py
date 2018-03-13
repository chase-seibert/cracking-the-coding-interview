#!/usr/bin/env python3

"""
Given two strings, is one at most one edit (insert, remove, replace) from
the other?

Completion time: 20 minutes.

Examples: "ab", "acb" (insert), "acb", "ab" (remove), "aaa", "aab" (replace).

Notes
- Note that insert and remove are the same case, just reversed inputs.
"""


def is_one_away(str1, str2):
    short, longer = str1, str2
    if len(str2) < len(str1):
        short, longer = str2, str1
    diff = 0
    # replace
    if len(short) == len(longer):
        for i in range(len(longer)):
            diff += int(longer[i] != short[i])
        return diff <= 1
    # insert AND remove
    elif len(short) == len(longer) - 1:
        j = 0
        for i in range(len(longer)):
            if longer[i] == short[j]:
                j += 1
            else:
                diff += 1
        return diff == 1
    # all other cases
    return False


if __name__ == '__main__':
    assert is_one_away('aaa', 'aab'), 'replace'
    assert is_one_away('ab', 'acb'), 'insert'
    assert is_one_away('acb', 'ab'), 'remove'
    assert not is_one_away('aa', 'bb')
