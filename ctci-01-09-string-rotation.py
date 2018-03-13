#!/usr/bin/env python3

"""
See if str2 is a rotation of str1 using ONE call to "is substring".

Completion time: 10 minutes.

Examples: "0abc", "bc0a"

Notes
- TRICK - str2 in (str1 + str1), assuming same length
"""


def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    return str2 in str1 + str1


def is_rotation_long(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        first, second = str1[:i], str1[i:]
        if str2 == second + first:
            return True
    return False


def is_rotation_long2(str1, str2):
    if len(str1) != len(str2):
        return False
    all_rotations = ''
    for i in range(len(str1)):
        first, second = str1[:i], str1[i:]
        all_rotations += second + first + ':'
    if str2 in all_rotations:
        return True
    return False


if __name__ == '__main__':
    assert is_rotation('0abc', 'bc0a')
    assert not is_rotation('1abc', 'bc0a')
    assert is_rotation_long('0abc', 'bc0a')
    assert is_rotation_long2('0abc', 'bc0a')
