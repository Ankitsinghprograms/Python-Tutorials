def pallindrone_list(n):
	
	if n<10:
		
		return n
		
	else:
		
		check=True
		
		while check:
			
			if str(n)==str(n)[::-1]:
				
				check=False
				
				no=n
				
			n+=1
			
		return no
		
		
l=[2,12,35,46,4293,3272,3626,5242]

p_l=list(map(pallindrone_list,l))

print(p_l)