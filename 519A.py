W={'Q':9,'R':5,'B':3,'N':3,'P':1,'K':0,'.':0,'q':0,'r':0,'b':0,'n':0,'p':0,'k':0}
B={'q':9,'r':5,'b':3,'n':3,'p':1,'k':0,'.':0,'Q':0,'R':0,'B':0,'N':0,'P':0,'K':0}
white=0
black=0
for i in range(8):
	s=raw_input()
	white=white+sum(map(lambda j: W[j],s))
	black=black+sum(map(lambda j: B[j],s))
if white>black:
	print "White"
elif black>white:
	print "Black"
else:
	print "Draw"			