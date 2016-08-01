n,m=map(int,raw_input().split())

row=set()
col=set()
for i in xrange(m):
	r,c=map(int,raw_input().split())
	row.add(r)
	col.add(c)
	print (n-len(row))*(n-len(col)),