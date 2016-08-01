s=raw_input().strip()
l=len(s)
dic={'A':'A','b':'d','d':'b','H':'H','I':'I','M':'M','O':'O','o':'o','p':'q','q':'p','T':'T','U':'U','V':'V','v':'v','W':'W','w':'w','X':'X','x':'x','Y':'Y'}
if l==1:
	try:
		if s==dic[s]:
			print "TAK"
			exit()
		else:
			print "NIE"
			exit()	
	except KeyError:
		print "NIE"
		exit()		
flag=True
for i in xrange((l/2)+1):
	try:
		if dic[s[i]]==s[l-1-i]:
			pass
		else:
			flag=False
			break
	except KeyError:
		flag=False		
if flag:
	print "TAK"		
else:
	print "NIE"

