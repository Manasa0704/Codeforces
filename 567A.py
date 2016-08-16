n=int(raw_input())
x=[-10**10]+map(int,raw_input().split())+[10**10]
print '\n'.join(map(lambda i:str(min(x[i]-x[i-1],x[i+1]-x[i]))+' '+str(max(x[i]-x[1],x[n]-x[i])),range(1,n+1)))
# for i in range(1,n-1):
# 	print min(x[i]-x[i-1],abs(x[i]-x[i+1])),max(x[i]-x[0],x[n-1]-x[i])
# print x[n-1]-x[n-2], x[n-1]-x[0]