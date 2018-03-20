#!/usr/bin/env python3

"""
String permutations, no dupes.

Completion time: 10 minutes.

Examples: 'abc' -> abc, acb, bac, bca, cab, cba

Notes
- Noticed that 6 possibilities == 2^3, smells like 2^n.
- I noticed that I manually iterated through each character, and appended it
  to the remaining permutations.
- Got the recursive call wrong, passed the string AFTER the first character
  instead of the string WITHOUT the current character (list comprehsion).
- Caching does save some calls
- Call out in the dupe case that if there are MANY dupes, you can optimize.
"""
import functools


@functools.lru_cache()
def str_perms(s):
    print('*')
    results = list()
    if len(s) == 1:
        return [s, ]
    for char in s:
        for perm in str_perms(''.join([c for c in s if c != char])):
            results.append(char + perm)
    return results


@functools.lru_cache()
def str_perms_dupes(s):
    # print('*')
    results = set()
    if len(s) == 1:
        return {s, }
    for i, char in enumerate(s):
        str_without_char_i = ''.join([s[j] for j in range(len(s)) if i != j])
        for perm in str_perms_dupes(str_without_char_i):
            results.add(char + perm)
    return results


if __name__ == '__main__':
    print(str_perms('abc'))
    print(str_perms_dupes('abca'))
