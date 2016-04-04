
inp=map(int,raw_input().split())
days=inp[0]
curr=0
prev=0
while(True):
	curr=days/inp[1]
	days=days+(curr-prev)
	if(curr-prev>0):
		prev=curr
	else:
		break	
	prev=curr

print days	



