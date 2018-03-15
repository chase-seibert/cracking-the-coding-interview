#!/usr/bin/env python3

"""
If all parents keep having kids until they get one girl, what is the eventual
populate ratio?

Completion time: 10 minutes.

Notes
- G, BG, BBG, BBBG...
- Assign a probabiity to each.
- Average expected number of girls == 1
- Averyage expected number of boys = 1*.25 + 2*.125 + 3*.0675 + 4*.03...
- Trends to 1, too.
- Makes sense, birth rate is still 50/50, doesn't matter when people stop. 
"""
