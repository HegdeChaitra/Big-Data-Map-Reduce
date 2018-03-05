#!/usr/bin/env python

import sys
import re
import csv

reader=csv.reader(sys.stdin,delimiter=',')
for words in reader:
	#line=line.strip()

	#words=line.split(',')
	#strg=words[-6]
	#if len(words[-6])==2:
	strg=words[-6]
	#elif len(words[-7])==2:
	#	strg=words[-7]
	#elif len(words[-8])==2:
	#	strg=words[-8]
	c=len(re.findall("NY",strg,re.IGNORECASE))
	#print(strg)
	#if words[16]=='NY' or words[16]=="ny" or words[16]=="nY" or words[16]=="Ny":
	if c>0:
		print ("{0}\t{1}".format(strg,1))
	else:
		print ("{0}\t{1}".format('Other',1))
