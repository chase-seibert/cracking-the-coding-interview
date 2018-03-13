#!/usr/bin/env python3

"""
Given a string, replace spaces with '%20' in place.

Completion time: 18 minutes.

Examples: 'ab c', 6 -> 'ab%20c', '', None, []

Notes
- Would use real url library.
- Would do input_str.replace(' ', '%20').
- In place string manipulation in python is an anti-pattern.
- So is index looping.
- Can't even do this in Python; strings are immutable
"""


def urlize(input_str, length):
    url = list(input_str + '.' * (length - len(input_str)))
    for i in range(len(url)):
        if url[i] != ' ':
            continue
        for j in range(len(url), i+1, -1):
            url[j-1] = url[j-3]
            url[j-2] = url[j-4]
        url[i] = '%'
        url[i+1] = '2'
        url[i+2] = '0'
    return ''.join(url)


if __name__ == '__main__':
    assert urlize('ab c', 6) == 'ab%20c', urlize('ab c', 6)
    assert urlize('a  b c', 12) == 'a%20%20b%20c'
