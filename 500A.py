n=map(int,raw_input().split())
cells=map(int,raw_input().split())

position=1
i=1
while (i<=n[0]):
	position=position+cells[i-1]
	if((position<n[1])):
		i=position
	elif (position==n[1]):
		print "YES"
		exit()
	else:
		print "NO"
		exit()
				


