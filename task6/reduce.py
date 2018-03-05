#!/usr/bin/env python

import sys

d={}
currentkey=None
count=0
for line in sys.stdin:

	line=line.strip()

	regid,value=line.split(',',1)
	#print(regid)
	#print(words[1])
	state,value=value.split('\t')
	#print(value)
	key=regid+','+state
	if currentkey==key:
		count=count+1
	else:
		if currentkey:
			#print('{}\t{}'.format(currentkey,count))
			d[currentkey]=count
		currentkey=key
		count=1
if currentkey==key:
	#print('{}\t{}'.format(currentkey,count))
	d[currentkey]=count

x=sorted(d,key=d.get,reverse=True)
for i in x[:20]:
	ss=i.split(',')
	print (str(ss[0])+","+" "+str(ss[1])+"\t"+str(d.get(i)))
#for j in x[-10:]:
#	ss=j.split(',')
#
#	print str(ss[0])+","+" "+str(ss[1])+"\t"+str(d.get(j))

