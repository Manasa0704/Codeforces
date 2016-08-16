n=int(raw_input())
a=map(int,raw_input().split())
c=0
for i in range(len(a)-1):
	print i,c
	if a[i]==0:
		c+=1
	else:	
		if a[i]==a[i+1] and a[i] in (1,2):
			c+=1
		elif a[i-1]==1 and a[i]==3 and a[i+1]==2:
			c+=1
		elif a[i-1]==2 and  a[i]==3 and a[i+1]==1:
			c+=1		
print c
