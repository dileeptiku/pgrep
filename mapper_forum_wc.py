#!/usr/bin/python
import sys
import csv
import re



#reader = csv.reader(sys.stdin, delimiter='\t')
#writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
myList = ""
cntf = 0
for line in sys.stdin:
   # YOUR CODE HERE
   # myList = re.split('; |, |. |? |: |\s |# |$ |= |- ',line)  
   line = line.strip();
  #myList = re.split('; |, |\s+ |. |\? \# \$ |= |- |\" |\(\) |\<\> |\[\]' ,line)
   myList = re.split("\W+",line)
   for word in myList:
      if word.upper() == 'FANTASTIC':
         cntf = cntf+1
print cntf


