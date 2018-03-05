#!/usr/bin/env python

import sys

currentkey=None
currval=None
prevkey=None
for line in sys.stdin:
	line=line.strip()
	key,value=line.split('\t',1)

	value=value.split('=')

	if currentkey==key:
		prevkey=currentkey

	else:
		if currentkey:
			if currentkey!=prevkey and currval[-1]=='parking':
				print ("{0}\t{1}, {2}, {3}, {4}".format(currentkey,currval[0],currval[1],currval[2],currval[3]))
		currentkey=key
		currval=value

if currentkey!=prevkey and currval[-1]=='parking':
        print ("{0}\t{1}, {2}, {3}, {4}".format(currentkey,currval[0],currval[1],currval[2],currval[3]))	
