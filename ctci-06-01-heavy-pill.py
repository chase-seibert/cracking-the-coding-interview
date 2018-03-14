#!/usr/bin/env python3

"""
Given 20 BOTTLES of pills, with 19 having 1.0g pills and 1 having 1.1g pills,
find the bottle with the 1.1g pills. You can use a kitchen scale ONCE.

Completion time: 20 minutes.

Notes
- Originally misunderstood and thought it was 20 total pills ;)
- New I needed different numbers of pills. Thought about primes, powers of two.
- Turns out that the total sum of pills was critical.
- 1 + 2 + 3 ... 20 == 210. I miscalculated as 209. (Sum == 20 * 21 in general)
- So label bottles 1,2,3 and put the corresponding number of pills in the scale.
- Subtract 210 and divide by 1.1 to figure out which pill bottle # the 1.1s are
  from.
"""
