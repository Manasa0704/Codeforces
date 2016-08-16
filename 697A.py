t,s,x=map(int,raw_input().split())

if ((x-t)%s==0 and (x-t)/s>=1) or ((x-t-1)%s==0 and (x-t-1)/s>=1) or (x==t):
	print "YES"
else:
	print "NO"	