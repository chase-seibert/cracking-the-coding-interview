#!/usr/bin/env python3

"""
Find the path from 0,0 to R,C in a maze, only going down and right.

Completion time: 25 minutes.

Notes
- Got basic algorith.
- Did not realize there could be dupe paths to the same point - memoize.
- Otherwise, runtime is 2^(r*c)
- Append a tuple to a tuple - need to cast to tuple
- Use nested tuples for matrix to make it hashable
"""

from functools import lru_cache


@lru_cache()
def find_path(m, cur, path):
    r, c = len(m)-1, len(m[0])-1
    cur_r, cur_c = cur
    if cur_r > r or cur_c > c or m[cur_r][cur_c] == 1:
        return None
    if cur_r == r and cur_c == c:
        return path
    for try_next in ((cur_r + 1, cur_c), (cur_r, cur_c + 1)):
        new_path = find_path(m, try_next, path + (try_next, ))  # append tuple
        if new_path:
            return new_path
    return None


if __name__ == '__main__':
    m = (
        (0, 0, 1, 0),
        (0, 0, 0, 0),
        (1, 0, 0, 0),
        (0, 0, 0, 0),
    )
    print(find_path(m, (0, 0), ((0, 0), )))
