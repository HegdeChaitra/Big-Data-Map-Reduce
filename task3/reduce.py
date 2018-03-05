#!/usr/bin/env python

import sys
import string
# import numpy
import os

currentkey = None
current_amount = 0
count = 0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

	#Remove leading and trailing whitespace
	line = line.strip()

	#Get key/value 
	key, amount = line.split('\t',1)
	try:
		amount = float(amount)
	except ValueError:
		continue

	#If we are still on the same key...
	if currentkey == key:
		current_amount += amount
		count += 1
		#Process key/value pair (your code goes here)

	#Otherwise, if this is a new key...
	else:
		#If this is a new key and not the first key we've seen
		if currentkey:
			print ('{0}\t{1:.2f}, {2:.2f}'.format(currentkey,round(current_amount,2),round(current_amount/count,2)))
			#compute/output result to STDOUT (your code goes here)
		currentkey = key	
		current_amount = amount
		count = 1
if currentkey == key:
	print ('{0}\t{1:.2f}, {2:.2f}'.format(currentkey,round(current_amount,2),round(current_amount/count,2)))
#Compute/output result for the last key (your code goes here)



