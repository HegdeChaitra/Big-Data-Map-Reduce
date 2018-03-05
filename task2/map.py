#!/usr/bin/env python

import sys
import csv

reader=csv.reader(sys.stdin,delimiter=',')
for words in reader:
	#line=line.strip()

	#words=line.split(',')

	print ("{0}\t{1}".format(words[2],1))
