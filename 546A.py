inputs=map(int,raw_input().split())
money=(inputs[0]*((inputs[2]*(inputs[2]+1))/2))-inputs[1]
if (money>0):
	print money
else:
	print 0	