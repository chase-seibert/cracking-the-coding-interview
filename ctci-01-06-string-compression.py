#!/usr/bin/env python3

"""
Compress a string by replacing repeated characters with counts, if shorter.

Completion time: 20 minutes.

Examples: "aabccc" -> "a2bc3", None, ""

Notes
- Similar to a problem I have asked?
"""


def compress(input_str):
    if not input_str:
        return input_str
    result, cur_char, cur_count = '', '', 0
    for char in input_str + '.':
        if char == cur_char:
            cur_count += 1
        if char != cur_char or char == '.':
            result += cur_char
            if cur_count > 1:
                result += str(cur_count)
            cur_char = char
            cur_count = 1
    if len(result) < len(input_str):
        return result
    return input_str


if __name__ == '__main__':
    assert compress('aabccc') == 'a2bc3'
    assert compress('abc') == 'abc'
    assert compress('') == ''
    assert compress(None) is None
