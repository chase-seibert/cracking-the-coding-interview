#!/usr/bin/env python3

"""
100 floors, 2 eggs. Find the floor the egg breaks at minimizing drops
for the worst case.

Completion time: 15 minutes.


Notes
- Second egg must always walk a range to find the exact floor.
- Binary search w/ first egg yields 49 drops worst case.
- Tried every 25 floors, but came to wrong conclusion.
- Should have been 25 (break = 24 more, total 25 or not break then try 50, etc)
  somewhere around 30 total drops, which is better.
- Then try 10, etc. Key insight is that you can "save" the first egg longer
  by going up in small increments from 0-100. 
- The mathematical right number is 14 drops. Can arrive their by trial and
  error, eventually.
"""
