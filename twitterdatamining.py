#!/usr/bin/python

import sys
import re
from collections import Counter 

test = []
languages = []
three = {}
cnt = Counter()
lng = Counter()

# input comes from STDIN 
for line in sys.stdin:
    line = line.strip()
    test = re.search('\[(.*?)\]',line).group(0)
    test = test[1:-1].replace("'","")
    test = test.split(",")
    for word in test:
        cnt[word.strip()] +=1

    line = line.split(",")
    if len(line) >=2:
        languages.append(line[2])
        three[line[0].strip()] = int(line[4].strip())
print '                                                                   '
print 'Top 10 popular users (those with the most number of followers) who have tweeted in the last hour' 
print '------------------------------------------------------------------'

for key, value in sorted(three.iteritems(), key=lambda item:(item[1], item[0]) , reverse=True)[:10]:
    print "%s: %s" % (key, value)

print '                                                                   '
print 'Top 10 trending individual hashtags across globe in the last hour'
print '------------------------------------------------------------------'
print cnt.most_common(10)

for ln in languages:
        lng[ln.strip()] +=1
print '                                                                   '
print 'Top 10 popular languages used across the globe in the last hour '
print '------------------------------------------------------------------'
print lng.most_common(10)
print '------------------------------------------------------------------'