s=str(raw_input())
#s='Hi!'
i=0
while i<len(s):
	if(s[i]=='H' or s[i]=='Q' or s[i]=='9'):
		print 'YES'
		exit()
	else:
		i+=1
print "NO"