#!/usr/bin/env python
import sys

pathCnt = 0
oldPath = None
highestPathCnt = ["path",0]

for line in sys.stdin:
    path = line.strip()
    if (oldPath == path): 
       pathCnt = pathCnt+1
    else: 
     oldPath = path 
     pathCnt = 1
    
    if (pathCnt>highestPathCnt[1]):
      highestPathCnt[0] = path
      highestPathCnt[1] = pathCnt



    
print highestPathCnt[0], "\t", highestPathCnt[1]  

