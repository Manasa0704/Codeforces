k=int(raw_input())
l=int(raw_input())
m=int(raw_input())
n=int(raw_input())
d=int(raw_input())
flag=0
for i in range(1,d+1):
	if(i%k==0 or i%l==0 or i%m==0 or i%n==0):
		flag+=1
print flag		