n,m=map(int,raw_input().split())
if n%2==0:
	a=n/2
	b=0
else:
	a=(n-1)/2
	b=1	

while (a>=0) and (b>=0):
	if (a+b)%m==0:
		break
	else:
		a-=1
		b+=2		
print [-1,a+b][a>=0 and b>=0]	
