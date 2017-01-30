#!/usr/bin/env python

import sys
#line = '10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 -'
#line = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] "GET / HTTP/1.1" 401 - "" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827"'

import re
#regex = '[(\d\.)]+ - - \[.*?\] ".*?" \d+ - ".*?" ".*?"'
regex = '([(\d\.)]+) (.*?|-) (.*?|-) \[(.*?)\] "(.*?)" (\d+) (\d+|-)'

#print(re.match(regex,line).groups())


for line in sys.stdin:
    data = re.match(regex,line).groups()
    if len(data) == 7:
       ip,cl,user, dw, url, rcode, dcode = data
       if (len(url.split(' ')) > 3):
          continue
       method, path, qrystr = url.strip().split(' ')
       if("http://www.the-associates.co.uk" in path and len(path)> 32):
          path = path.strip()[31:]	
       print ("{0}".format(path))

