#!/usr/bin/env python3

"""
Implement an algorithm to determine if a string has only unique characters.
What if you cannot use additional data structures?

Completion time: 21 minutes.

Examples: 'cats', 'catsa', '', None, [], ['a', 'b']

Notes
- Was not sure set('abc') would work (it does).
- What does len(None) do? TypeError.
- What is the fastest sort? Quicksort: nlog(n)
- 'str' is NOT a good name (reserved word)
- Initially reverse the True/False in the gen version
"""


def has_only_unique_chars(input_str):
    return len(input_str) == len(set(input_str))


def has_only_unique_chars_gen(input_str):
    unique_chars = set()
    for char in input_str:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    return True


if __name__ == '__main__':
    assert has_only_unique_chars('abc')
    assert not has_only_unique_chars('abcb')
    assert has_only_unique_chars(['a', 'b'])
    assert has_only_unique_chars_gen('abc')
