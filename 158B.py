from __future__ import division
import math
import fileinput
s=8
a=[2,3,4,4,2,1,3,1]
data=[0,0,0,0]
for temp in a:
	if temp==1:
		data[0]+=1
	elif temp==2:
		data[1]+=1
	elif temp==3:
		data[2]+=1
	else:
		data[3]+=1

taxi=data[3]+data[2]
data[0]=data[0]-data[2]
if data[0]>0:
	taxi=taxi+math.ceil((2*data[1]+data[0])/4)
else:
	taxi=taxi+math.ceil(data[1]/2)

print a
print data
print int(taxi)