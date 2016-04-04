#a=str(raw_input())
#b=str(raw_input())
a='aaaa'
b='aaaA'

a=a.lower()
b=b.lower()
i=0
string1=0
string2=0
while i<len(a):
	if(ord(a[i])==ord(b[i])):
		i+=1
	elif(ord(a[i])>ord(b[i])):
		print 1
		exit()
	else:
		print -1
		exit()
print 0							