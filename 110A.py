n=long(raw_input())
lucky=0
while n>0:
	r=n%10
	n=n/10
	if(r==4 or r==7):
		lucky+=1
	else:
		pass
if(lucky==4 or lucky==7):
	print "YES"
else:
	print "NO"				