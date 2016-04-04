array=map(int,raw_input().split())
duration=array[0]
remainder=0
while (array[0]>=array[1]):
	remainder=(array[0]%array[1])
	array[0]=array[0]/array[1]
	duration=duration+array[0]
	array[0]=array[0]+remainder
print duration
