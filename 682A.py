n,m=map(int,raw_input().split())
ans=0
for i in xrange(1,n+1):
	ans=ans+ (m+i)/5 - i/5
print ans