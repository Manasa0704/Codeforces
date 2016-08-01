n,m=map(int,raw_input().split())
c=map(int,raw_input().split())
t=map(int,raw_input().split())
d=[0]*n
# def g_val(val,t):
# 	v=10**10
# 	for i in xrange(m-1,-1,-1):
# 		if val<=t[i]:
# 			v=t[i]
# 		else:
# 			break
# 	return v

def l_val(val,t):
	i=0
	for i in t:
		if val>=i:
			a=i
		else:
			break			
	return i-1				
for i in range(n):
	b=l_val(c[i],t)
	a=g_val(c[i],t)
	d[i]=min(a-c[i],c[i]-b)
print max(d)
