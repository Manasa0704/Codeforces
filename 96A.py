import math
import fileinput

n=str(raw_input())
t=0
flag=0
if len(n)<=7:
	print 'NO'
	exit()
prev=n[0]
for i in n:
	cur=i
	if(prev==cur):
		t+=1
	else:
		t=1
	prev=cur
	if t==7:
		flag=1
		break

if flag==1:
	print 'YES'
else:
	print 'NO' 

