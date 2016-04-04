import string
str_input=raw_input()
i=0
output=''
flag=False
while(i<len(str_input)):
	if(str_input[i:i+3]=='WUB'):
		i+=3
		if flag==True:
			output=output+" "
	else:
		flag=True
		output=output+str_input[i]
		i+=1

print output

			