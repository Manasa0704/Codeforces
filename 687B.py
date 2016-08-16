n,k=map(int,raw_input().split())
c=list(map(int,raw_input().split()))
r=[]
c_min=min(c)
for i in c:
	for j in range(n/c_min):
		r.append((j*i+(n%i))%k)

print ["No","Yes"][len(set(r))==1 or k in c]

