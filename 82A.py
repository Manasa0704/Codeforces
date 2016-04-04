import math
n=long(raw_input())
lower=int(math.log(math.ceil(float(n)/5),2))
limit=pow(2,lower)
index=int(math.ceil((n-5*(limit-1))/float(limit)))
big_bang=['','Sheldon','Leonard','Penny','Rajesh','Howard']
print big_bang[index]


