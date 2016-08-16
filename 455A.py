n=raw_input()
a=map(int,raw_input().split())
# print a
counter=[0]*10002
for i in a:
	counter[i]+=i
final=0

while sum(counter)>0:
	max_points=0
	for i in range(1,len(counter)):
		if counter[i]!=0:
			# print i
			if i*counter[i]>max_points:
				max_points=i*counter[i]
				index=i
		else:
			pass		
	counter[index]=0
	counter[index-1]=0
	counter[index+1]=0
	final=final+max_points

print final    




