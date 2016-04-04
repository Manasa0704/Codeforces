n=26
init=[0]*26
s=str(raw_input())
i=0
total=0
while i<len(s):
	init[ord(s[i])-97]+=1
	i+=1
for i in range(26):
	if(init[i]!=0):
		total+=1

if total%2==0:
	print 'CHAT WITH HER!'
else:
	print 'IGNORE HIM!'	

