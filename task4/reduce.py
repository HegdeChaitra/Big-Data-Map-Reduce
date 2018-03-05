#!/usr/bin/env python

import sys

count=0
currentkey=None
for line in sys.stdin:
	line=line.strip()
	key,value=line.split('\t')
	#print(words[0])
	if currentkey==key:
		count=count+1
	else:
		if currentkey:
			print ("{0}\t{1}".format(currentkey,count))
		currentkey=key
		count=1
if currentkey==key:
	print ("{0}\t{1}".format(currentkey,count))
