n=int(raw_input())
arr=map(int,raw_input().split())
length=[]
count=1
i=0
while(i<n-1):
	if(arr[i+1]>=arr[i]):
		count+=1
	else:
		length.append(count)
		count=1
	i+=1	
length.append(count)	
print max(length)


