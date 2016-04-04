inp=map(int,raw_input().split())
quant=map(int,raw_input().split())
temp=sorted(quant,reverse=True)
diff=[]
if (inp[0]==inp[1]):
	print (temp[0]-temp[inp[0]-1])
else:	
	for i in range(0,inp[1]-inp[0]+1,1):	
		diff.append(temp[i]-temp[i+(inp[0]-1)])
	print min(diff)	