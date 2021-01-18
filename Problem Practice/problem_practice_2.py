n,mn,mx=input().split()

for i in range(int(mn),int(mx)+1):
	
	if int(n)%i==0:
		
		print(i,"is a divisior of ",n)
	
	else:
		
		print(i,"isn't a divisior of",n)