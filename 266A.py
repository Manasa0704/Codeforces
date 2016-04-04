#n=int(raw_input())
#string=str(raw_input())
string='BRBG'
i=1
num=0
prev=string[0]
while i<len(string):
	if(string[i]==prev):
		num+=1
	prev=string[i]
	i+=1
print num	

