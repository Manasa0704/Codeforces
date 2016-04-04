grid=map(int,raw_input().split())
count=0
net=grid[0]*grid[1]
while(net>=1):
	net=(grid[0]*grid[1])-(grid[0]+grid[1]-1)
	grid[0]-=1
	grid[1]-=1
	count+=1
if(count%2!=0):
	print "Akshat"
else:
	print "Malvika"		