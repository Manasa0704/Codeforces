n=int(raw_input())
flag=0
num_set=[4,7,44,47,74,77,444,447,477,744,747,777]
for i in num_set:
	if(i<=n):
		if(n%i==0):
		   flag+=1
		else:
			pass
	else:
		break		   


if flag!=0:
	print "YES"
else:
	print "NO"
