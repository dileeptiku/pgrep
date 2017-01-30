#!/usr/bin/env python
import sys

totalsales  = 0
oldKey = None
salescnt = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data
    thisSale = float(thisSale)
    totalsales = totalsales + thisSale
    salescnt = salescnt+1



print salescnt, "\t", totalsales

