n=int(raw_input())
arr=[]
for i in range(n):
	temp=map(int,raw_input().split())
	arr.append(temp)

count=0
for i in range(n):
	for j in range(n):
		if(arr[i][0]==arr[j][1]):
			count+=1
		else:
			pass

print count				