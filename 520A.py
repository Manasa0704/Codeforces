def count(s,string):
	count=0
	for i in string:
		if i==s:
			count+=1
	return count
	
if __name__ == '__main__':			
	length=int(raw_input())
	string=raw_input().lower()
	if length<26:
		print "NO"
		exit()

	dictionary=dict((i,count(i,string)) for i in string)
	if len(dictionary)==26:
		print "YES"
	else:
		print "NO"	

