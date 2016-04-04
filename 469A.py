n=int(raw_input())
X=map(int,raw_input().split())
Y=map(int,raw_input().split())

for i in range(1,n+1):
	if ((i in X[1:len(X)+1]) or (i in Y[1:len(Y)+1])):
		pass
	else:
		print "Oh, my keyboard!"		
		exit()	

print "I become the guy."



