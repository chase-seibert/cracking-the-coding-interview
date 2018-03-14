#!/usr/bin/env python3

"""
Given three ants on three points of a triangle, if they start walking in
a random direction, what is the probability then will collide?

Completion time: 10 minutes.

Notes
- Listed out all the options.
- Obvious quickly that they need to all walk in the same direction.
- 2 possibilities they do not collide, 6 possibilities that they do.
- Miscalculated as 1/3 instead of 1/4.
- Tried for 2 ants on a line/log, got 1/2.
- Generalized to 1/(2^(n-1)), but did not prove it.
- Again, should have thought of it as .5*.5*.5 * 2 (directions)
"""
