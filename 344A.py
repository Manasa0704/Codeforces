n=int(raw_input())
arr=[]
for i in range(n):
	temp=int(raw_input())
	arr.append(temp)

count=1
for i in range(n-1):
	if(arr[i+1]!=arr[i]):
		count+=1
	else:
		pass
 
print count			 	