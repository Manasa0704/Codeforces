n=raw_input()
s=raw_input().split()
i=1
s.sort(key=int)
while i<=n:
	if(sum(int(j) for j in s[:len(s)-i])<sum(int(j) for j in s[len(s)-i:len(s)])):
		print i
		exit()
	else:
		i+=1


