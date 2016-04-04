n=int(raw_input())
vector=[0]*3
for i in range(n):
	temp=map(int,raw_input().split())
	for i in range(3):
		vector[i]=vector[i]+temp[i]
if(vector[0]==0 and vector[1]==0 and vector[2]==0):
	print "YES"
else:
	print "NO"	 		