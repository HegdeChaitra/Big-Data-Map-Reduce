#!/usr/bin/env python
 
import sys
import string
import csv
import os

reader=csv.reader(sys.stdin,delimiter=',')
weekend = [5,6,12,13,19,20,26,27]
for entry in reader:
    
	#Remove leading and trailing whitespace
	#line = line.strip()

	#Split line into array of entry data
	#entry = line.split(",")
    
	# Set row, column, and value for this entry
	key = entry[2]
	value1 = 1
	try:
		value2 = entry[1].split("-")[2]
		value2 = int(value2)
	except ValueError:
		continue
	if value2 in weekend:
		day = 'weekend'
	else:
		day = 'weekday'
	print ('{0:s}\t{1:d},{2:s}'.format(key,value1,day))



	
        
