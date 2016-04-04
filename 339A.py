s=str(raw_input())
i=0
out=''
list1=[0,0,0]
while i<len(s):
	if(s[i]!='+'):
		list1[int(s[i])-1]+=1
	i+=1
i=0		
j=0
for i in range(3):
	for j in range(list1[i]):
		out=out+str(i+1)+'+'


print str(out[:len(out)-1])



