#!/usr/bin/env python

import sys
import string
import os

currentkey = None
current_count = 0
current_column = None
dict_color = {}
dict_make = {}
for line in sys.stdin:
	line = line.strip()

	#Get key/value 
	column,key,count = line.split('^^',2)
#	print(current_column)
#	print(value)
	#value = value.split('=')
	#key, count = value[0], value[1]
	try:
		count = int(count)
	except ValueError:
		continue
	
	if currentkey == key:
		current_count += count
		

	
	else:
	
		if currentkey:
			
			if current_column == 'make':
				dict_make[currentkey] = current_count
			else:
				dict_color[currentkey] = current_count 
			
		currentkey = key
		current_count = count
		current_column = column 
if currentkey == key:
	
	if current_column == 'make':
		dict_make[currentkey] = current_count
	else:
		dict_color[currentkey] = current_count


sorted_dict_color = sorted(dict_color.items(),key = lambda x: x[0])
sorted_dict_make = sorted(dict_make.items(),key = lambda x: x[0])

for i in sorted_dict_make:
	print ('vehicle_make\t{0:s}, {1:d}'.format(i[0],i[1]))

for i in sorted_dict_color:
	print ('vehicle_color\t{0:s}, {1:d}'.format(i[0],i[1]))



