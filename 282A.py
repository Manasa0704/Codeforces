import math
import fileinput

n=int(raw_input())
x=0
for i in range(n):
	a=raw_input()
	if (a=='++X' or a=='X++'):
		x+=1
	else:
		x-=1
print x