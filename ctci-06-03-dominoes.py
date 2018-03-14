#!/usr/bin/env python3

"""
Given an 8x8 checker board with two opposite corners cut out, and 31 domioes
which can each cover two spots, can you cover the entire board?

Completion time: 15 minutes.

Notes
- Tried on 4x4 first, convinced you cannot manually.
- Tried 2x2, obviously not.
- Could not prove it past intuition.
- First hint - count number of white/black spots.
- Turns out that opposite corners MUST be the same color.
- So, 8x8 board means 6 black spots, 8 white spots open.
- Each dominoe MUST cover one white and one black - can't work.
"""
