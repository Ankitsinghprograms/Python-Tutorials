for i in range(int(input())):
	
	no=int(input())
	
	check=True
	
	while check:
		
		if str(no)==str(no)[::-1]:
			check=False
			
			print(f"Next pallindrone is {no}")
			
		no+=1