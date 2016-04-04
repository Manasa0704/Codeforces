import math
import fileinput

n=int(raw_input())
temp=0
cap=0
for i in range(n):
	a=int(raw_input().split())
	temp=temp+(a[1]-a[0])
	if(cap<temp):
		cap=temp
print cap		
