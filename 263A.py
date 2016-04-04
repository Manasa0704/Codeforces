import math
matrix=[]
for i in range(5):
	matrix.append([])
 	temp=raw_input().split()
 	for j in range(5):
 		if temp[j]=='1':
 			print abs(2-i)+abs(2-j)
 			exit()



