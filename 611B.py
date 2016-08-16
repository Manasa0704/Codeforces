s,e=map(int,raw_input().split())
c=bin(s)[2:]
ans=0
for i in xrange(2,64):
	for j in xrange(2,i):
		a=int('1'*i+'0'+'1'*(j-i-1),2)
		if s<=a<=e:
			print a
# for i in xrange(s,e+1):
# 	print i
# 	c=bin(i)[2:]
# 	if c.count('0')==1:
# 		ans+=1
# print ans		