#!/usr/bin/env python3

"""
Tallest height stack of a list of boxes, given that W,H,D must all be larger
for the lower boxes.

Completion time: 20 minutes.

Notes
- Recursive solution, keep track of max W,H,D and tally H as you go.
"""
import sys
from functools import lru_cache


@lru_cache()
def height_tallest_stack(boxes, last_box=None, total_height=0):
    # print('*')
    last_box = last_box or (sys.maxsize, sys.maxsize, sys.maxsize)
    last_w, last_h, last_d = last_box
    last_height = total_height
    for box in boxes:
        w, h, d, = box
        if w < last_w and h < last_h and d < last_d:
            other_boxes = tuple(list(b for b in boxes if b != box))
            new_height = height_tallest_stack(other_boxes, box, last_height+h)
            if new_height > total_height:
                total_height = new_height
    return total_height


if __name__ == '__main__':
    boxes = (
        (1, 1, 1),
        (2, 2, 2),
        (3, 3, 3),
        (1, 1, 1),  # ignored
    )
    print(height_tallest_stack(boxes))  # should be 3 + 2 + 1 == 6
