n,x=map(int,raw_input().split())
print sum([1 for i in range(1,n+1) if (x%i==0) and (x/i)<=n])
