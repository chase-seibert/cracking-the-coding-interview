#!/usr/bin/env python3

"""
100 lockers, 100 passes. On each pass, toggle the I'th lockers. How many are
open at th end?

Completion time: 15 minutes.

Notes
- Tried it for 10 lockers.
- First, made mistake that not every other locker is toggled in 3+ pass.
- Corrected.
- Open lockers are 1, 4, 9 -> 3 total lockers.
- Knew that toggles had to be odd, which means odd number factors.
  Got stuck there.
- Turns out that odd factors means two factors paired with each other, plus
  the "perfect" factor where there is no pair (ex: 1x1, 2x2, 3x3, 4x4, etc).
- Question is how many perfect squares between 1-100.
- List them: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 == 10 lockers.
"""
