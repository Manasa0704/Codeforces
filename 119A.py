def gcd(a,b):
	while b!=0:
		(a,b)=(b,a%b)
	return a	

if __name__=="__main__":
	turn=0
	inputs=map(int,raw_input().split())
	while(True):
		if(turn%2==0):
			inputs[2]=inputs[2]-gcd(inputs[2],inputs[0])
			if(inputs[2]<0):
				print 1
				break
			else:
				turn+=1
		else:
			inputs[2]=inputs[2]-gcd(inputs[2],inputs[1])
			if(inputs[2]<0):
				print 0
				break
			else:	
				turn+=1
			

