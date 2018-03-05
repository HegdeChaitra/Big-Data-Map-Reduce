#!/usr/bin/env python

import sys
import string
# import numpy
import os

currentkey = None
current_sum_weekday = 0
current_sum_weekend = 0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

	#Remove leading and trailing whitespace
	line = line.strip()

	#Get key/value 
	key, value = line.split('\t',1)
	value = value.split(',')
	count , day = value[0], value [1]
	try:
		count = int(count)
	except ValueError:
		continue
	#If we are still on the same key...
	if currentkey == key:
		if day =='weekend':
			current_sum_weekend += count
		else:
			current_sum_weekday += count
		#Process key/value pair (your code goes here)

	#Otherwise, if this is a new key...
	else:
		#If this is a new key and not the first key we've seen
		if currentkey:
			print ('{0}\t{1:.2f}, {2:.2f}'.format(currentkey,float(current_sum_weekend)/8,float(current_sum_weekday)/23))
			#compute/output result to STDOUT (your code goes here)
		currentkey = key
		if day == 'weekend':	
			current_sum_weekend = count
			current_sum_weekday = 0
		else:
			current_sum_weekday = count
			current_sum_weekend = 0 
if currentkey == key:
	print ('{0}\t{1:.2f}, {2:.2f}'.format(currentkey,float(current_sum_weekend)/8,float(current_sum_weekday)/23))
#Compute/output result for the last key (your code goes here)




