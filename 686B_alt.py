n=int(raw_input())
a=map(int,raw_input().split())
i=0
flag=1
while flag>0:
	flag=0
	while(i<n-1):
		if a[i]>a[i+1]:
			print i+1, i+2
			a[i],a[i+1]=a[i+1],a[i]
			i+=2
			flag+=1
		else:
			i+=1
	i=0



