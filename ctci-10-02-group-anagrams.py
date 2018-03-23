#!/usr/bin/env python3

"""
Sort list of words grouping anagrams together.

Completion time: 5 minutes.

Examples: ['abc', 'bc', 'bac', 'cb']

Notes
- Noticed right away that if you sorted each word, you could then sort the
  list. O(nlog(n)
- Trick: could also create a hash of "abc" -> ["abc", "bac"], then merge lists
  in any order. Would be O(n).
"""


def sort_anagrams(words):
    return sorted(words, key=sorted)


if __name__ == '__main__':
    print(sort_anagrams(['abc', 'bc', 'bac', 'cb']))
