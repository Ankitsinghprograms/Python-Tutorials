
l=[a for a in range(100) if a%2==0]

s={a for a in {1,2,3,1,2,3,1,2,3}}

d={i:f"key {i}" for i in range(100)}

d={value:key for key,value in d.items()}

g=(i for i in range(1000) if i%5==0)



print(l,s,d,[each for each in g],sep="\n")








l=[]

while True:
	
	a=input("Enter no of items you want to append in list: ")
	
	try:
		
		a=int(a)
		print()
		break
	except:
		
		print("Please Enter correct no\n")
		
print("Enter 1 for list comperehension\n")

print("Enter 2 for set comperehension\n")
		

print("Enter 3 for dictionary comperehension\n")

print("Enter 4 for generator Comperehension\n ")

option=input()
print()
if option=="1":
	
	l=[i for i in range(a)]
	
	print(l)
	
	
elif option=="2":
	
	s={i for i in range(a)}
	
	print(s)
	
	
elif option=="3":
	
	d={i:f"key {i}" for i in range(a)}
	
	d={value:key for key,value in d.items()}
	
	print(d)
	
else:
	
	g=(i for i in range(a))
	
	for each in g:
		
		print(each,end=" ")