def rohanmultiplication(n):
	
	t1=[]
		
	t1.append((n*1)+2)
		
	t1.append((n*2))
		
	t1.append((n*3))
		
	t1.append((n*4)+1)
		
	t1.append((n*5))
		
	t1.append((n*6)+3)
		
	t1.append((n*7)+2)
		
	t1.append((n*8))
		
	t1.append((n*9))
		
	t1.append((n*10)+2)
		
	return t1
		
		
def isCorrect(table,n):
		
	correct_table=[n*i for i in range(1,11)]
	i=1
	for each in table:
		
		if each==(n*i):
			
			print(f"{n} times {i} is {each}")
		
		else:
			
			print(f"{n} times {i} is {each} !!Wrong    \t{n} times {i} is {n*i}")
			
		i+=1
		
try:
	i=int(input("Enter any no.\n\n"))
	
except:
	
	print("Wrong input!!\n")
	
	exit()
	
a=rohanmultiplication(i)

b=isCorrect(a,i)
