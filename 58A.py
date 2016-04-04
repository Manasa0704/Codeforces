s=str(raw_input())
ind_h=s.find('h')
ind_e=s.find('e',ind_h+1)
ind_l1=s.find('l',ind_e+1)
ind_l2=s.find('l',ind_l1+1)
ind_o=s.find('o',ind_l2+1)
if (ind_h!=-1 and ind_e!=-1 and ind_l1!=-1 and ind_l2!=-1 and ind_o!=-1):
	print 'YES'
else:
	print 'NO'	
