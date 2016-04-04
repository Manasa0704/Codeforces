def composite(number):
	divisor=2
	flag=False
	while (divisor<number): 
		if(number%divisor==0):
			flag=True
			break
		else:
			divisor+=1	
	return flag		


if __name__=='__main__':
	n=int(raw_input())
	flag=False
	if(n%2==0):
		print "4"+" "+str(n-4)
	else:
		test=4
		while (flag!=True): 
			flag=composite(n-test)	
			if (flag)
:				print str(test)+" "+str(n-test)
				exit
			else:
				test+=2	