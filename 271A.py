year=int(raw_input())
flag=False
value=year+1
while(True):
	temp=value
	u=temp%10
	temp=temp/10
	t=temp%10
	temp=temp/10
	h=temp%10
	temp=temp/10
	th=temp
	if(u!=t and u!=h and u!=th and t!=h and t!=th and h!=th):
		print value
		break
	else:
		value=value+1	

