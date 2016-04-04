from __future__ import print_function
n=int(raw_input())
array=raw_input().split()
output=[0]*n
for i in range(1,n+1):
	output[int(array[i-1])-1]=i
print (*output, sep=' ')	


