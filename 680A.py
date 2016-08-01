a=map(int,raw_input().split())
a.sort()
print a
s=sum(a)
print s
dic={}
for i in xrange(len(a)-1,-1,-1):
	if a[i] in dic.keys():
		dic[a[i]]+=1
	else:
		dic[a[i]]=1
m=s
for key,value in dic.iteritems():
	if value>=2:
		s=s-