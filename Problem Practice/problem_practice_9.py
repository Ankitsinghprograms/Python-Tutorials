import random

l=[]
t=[]

for i in range(int(input("Enter total no of Friends\n\n"))):
	
	l.append(input("Enter Your friend name\n\n").split())
	
	t.append(i)
i=0

for each in l:
	
	while True:
		
		r=random.choice(t)
		
		if r!=i:
			
			break
		
	try:
		
		print(each[0],*l[r][1:])
	
		t.remove(r)
		
	except:
		
		pass
		
	i+=1