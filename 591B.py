import string
n,m=map(int,raw_input().split())
name=raw_input()
alph= string.ascii_lowercase
for j in range(m):
	x,y=raw_input().split()
	alph=alph.translate(string.maketrans(x+y,y+x))
old_alph=string.ascii_lowercase	
print name.translate(string.maketrans(old_alph,alph))
