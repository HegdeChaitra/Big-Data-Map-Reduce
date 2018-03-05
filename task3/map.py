#!/usr/bin/env python
 
import sys
import string
import csv
import os

reader=csv.reader(sys.stdin,delimiter=',')
# input comes from STDIN (stream data that goes to the program)
for entry in reader:
    
	#Remove leading and trailing whitespace
	#line = line.strip()

	#Split line into array of entry data
	#entry = line.split(",")
    
	# Set row, column, and value for this entry
	key = entry[2]
	try:
		value = float(entry[12])
	except ValueError:
		continue

	print ('{0:s}\t{1:f}'.format(key,value))

	
        
