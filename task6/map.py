#!/usr/bin/env python

import sys
import csv

reader=csv.reader(sys.stdin,delimiter=',')

for words in reader:

	#line=line.strip()
	#words=line.split(',')
	if words[-8]=="":
		continue
	print ("{0},{1}\t{2}".format(words[-8],words[-6],1))
