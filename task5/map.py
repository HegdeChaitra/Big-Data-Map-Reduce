#!/usr/bin/env python

import sys
import csv

reader=csv.reader(sys.stdin,delimiter=',')
for words in reader:

	#line=line.strip()
	#words=line.split(',')
	print ("{0}, {1}\t{2}".format(words[14],words[16],1))
