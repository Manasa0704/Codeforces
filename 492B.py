n,l=map(int,raw_input().split())
lanterns=map(int,raw_input().split())
lanterns.sort(key=int)
diff=[lanterns[i+1]-lanterns[i] for i in range(len(lanterns)-1)]
if not diff:
	diff=[0]
print max(lanterns[0],l-lanterns[-1],max(diff)/float(2))