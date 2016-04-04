s=str(raw_input())
#s='Lock'
i=1
flag=0
while i<len(s):
	if (s[i]!=s[i].upper()):
		break
	i+=1
	flag+=1	
if (flag==len(s)-1 and s[0]==s[0].lower()):
	s=s.title()
	print s
elif(flag==len(s)-1 and s[0]==s[0].upper()):
	s=s.lower()
	print s
else:
	print s	








