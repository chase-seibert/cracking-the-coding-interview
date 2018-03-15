#!/usr/bin/env python3

"""
1000 bottles, 1 poisoned. 10 test strips, 7 days for each test.

Completion time: 30 minutes.

Notes
- Got brute force solution of 1000 days, and search solution of 28 days.
- Did not see that you can encode 1024 variations in 10 bits.
- Encode each bottle number into binary.
- Give each strip a position in the binary value tp 1024.
- If there is a 1 in that postion, add a drop from that bottle.
- After ONE round of testing, read strips out for bottle number in binary.
- The HINT that binary would be involved is that test strips are 0/1, and
  1000 < 1024, which is 2^10. 
"""
