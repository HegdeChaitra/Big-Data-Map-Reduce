#!/usr/bin/env python

import sys


currentkey=None
count=0
d={}
for line in sys.stdin:

	line=line.strip()

	key,value=line.split('\t',1)
	
	if currentkey==key:
		count=count+1
	else:
		if currentkey:
			#ff=currentkey.split(',')
			#print "{0}, {1}\t{2}".format(ff[0],ff[1],count)
			d[currentkey]=count
		currentkey=key
		count=1
if currentkey==key:
	#fd=currentkey.split(',')
	#print "{0}, {1}\t{2}".format(fd[0],fd[1],count)
	d[currentkey]=count
sd=sorted(d.items(),key = lambda x: x[1], reverse=True)
print ("{0}\t{1}".format(sd[0][0],sd[0][1]))
