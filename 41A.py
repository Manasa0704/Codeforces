import string
import math
def reverse(s,left,right,l):
	temp=s[left]
	s[left]=s[right]
	s[right]=temp
	left-=1
	right+=1
	if(left==-1 and right==l):
		return s
	else:
		reverse(s,left,right,l)
		return s


if __name__=='__main__':
	s=map(list,raw_input())
	t=raw_input()
	l=len(s)
	if(l==1):
		out=s
	elif(l%2==0):
		out=reverse(s,int((l/2)-1),int((l/2)),l)
	else:
		out=reverse(s,int(math.floor(l/2))-1,int(math.ceil((l/2)))+1,l)
	
	output=''.join(str(element) for sub in out for element in sub)
	
	if (t==output):
		print "YES"
	else:
		print "NO"	







