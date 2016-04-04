n=int(raw_input())
arr=map(int,raw_input().split())

min_index=0
max_index=0
for i in range(n-1):
	if(arr[i+1]<=arr[min_index]):
		min_index=i+1
	else:
		pass

	if(arr[i+1]>arr[max_index]):
		max_index=i+1
	else:
		pass

if(min_index>max_index):
	print (max_index)+(n-1-min_index)	
else:	
	print (max_index-1)+(n-1-min_index)			