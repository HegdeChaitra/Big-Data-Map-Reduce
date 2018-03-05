#!/usr/bin/env python
 
import sys
import string
import csv
import os

reader=csv.reader(sys.stdin,delimiter=',')
# input comes from STDIN (stream data that goes to the program)
for entry in reader:
    
	#line = line.strip()
	#entry = line.split(",")
	#print(entry)
	#if len(entry)==22:
	key1 = entry[-2]
	key2 = entry[-3]
	#else:
		#if len(key1)<2:
		#	key1=entry[-4]+","+entry[-3]
		#print("-------------")
		#print(key2,len(key2))
		#print(entry)
		#print(len(entry))
		#key1=entry[-3]
		#key2=entry[-4]
		#if len(key2)<2:
		#	key2=entry[-4]+","+entry[-3]
		#print(key1,key2)
	value11 = 1
	value12 = 'make'
	value21 = 1
	value22 = 'color'
	if key1=="" or key1==" ":
		key1="NONE"
	if key2=="" or key2==" ":
		key2="NONE"
#	if len(key1) != 0:
	print ('{0}^^{1}^^{2}'.format(value12,key1,value11))
	#if len(key2) != 0:
	print ('{0}^^{1}^^{2}'.format(value22,key2,value21))



	
        
