#!/usr/bin/env python3

"""
Classic tower of hanoi, moved all disks from t1 to t3.

Completion time: 30 minutes.

Examples: 1/3/5

Notes
- Needed all the hints, but ended up with solution.
- Two base cases: move 1 disk from any tower to another, and move 2 disks from
  any tower to another using a buffer tower.
- Cases beyond that move n-1 disks.
"""


def move(num_disks, src, dst, buf):
    if num_disks == 0:
        return
    elif num_disks == 1:
        dst.append(src.pop())
        print_towers(src, dst, buf)
    elif num_disks == 2:
        buf.append(src.pop())
        dst.append(src.pop())
        dst.append(buf.pop())
        print_towers(src, dst, buf)
    else:
        move(num_disks-1, src, buf, dst)
        dst.append(src.pop())
        move(num_disks-1, buf, dst, src)


def print_towers(src, dst, buf):
    print('src: ', src)
    print('buf: ', buf)
    print('dst: ', dst)
    print('====')


if __name__ == '__main__':
    src, buf, dst = [5, 4, 3, 2, 1], [], []
    print_towers(src, dst, buf)
    move(5, src, dst, buf)
    print_towers(src, dst, buf)
