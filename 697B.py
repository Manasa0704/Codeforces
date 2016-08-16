number=raw_input()
x=number.index('e')
y=number.index('.')
a=number[:y]
d=number[y+1:x]
b=int(number[x+1:])
if b==0 and int(a)==0 and int(d)==0:
	print 0
	exit()
if int(d)==0:
	print a+'0'*(b)
elif len(d)>b:
	print a+d[:b]+'.'+d[b:]
else: 
	print a+d+'0'*(b-len(d))