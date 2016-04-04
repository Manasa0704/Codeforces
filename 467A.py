n=int(raw_input())
flag=0
for i in range(n):
	room=raw_input().split()
	if(int(room[1])-int(room[0])>=2):
		flag+=1
	else:
		pass
print flag			