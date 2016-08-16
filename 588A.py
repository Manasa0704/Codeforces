
n=int(raw_input())
cost=0
min_c=101
for i in range(n):
	t1,t2=map(int,raw_input().split())
	min_c=min(t2,min_c)
	cost=cost+t1*min_c
print cost		
