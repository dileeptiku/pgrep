#!/usr/bin/env python
import sys

highestSale  = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data
    thisSale = float(thisSale)

    if thisSale > highestSale:
      highestSale = thisSale

    if oldKey and oldKey != thisKey:
      print oldKey, "\t", highestSale
      oldKey = thisKey
      highestSale = 0

    oldKey = thisKey

if oldKey != None:
    print oldKey, "\t", highestSale

