#Your age in 2090
c_y=2021

try:
	
	f=input("Enter your age or your birth year\n")
	
	first=int(f)
	
except:
	
	print("Wrong Input!!!")

birth_year=0

age=0

if len(f)==4:
	
	birth_year=first
	
	if birth_year>c_y:
		
		print("You are'nt born yet!!")
		
		exit()

	birth_year=first
	
	age=c_y-birth_year
	
	if age>150:
		
		print("You are oldest person alive\n")
		
		exit()
	
else:
	
	age=first
	
	if age>150:
		
		print("You are oldest person alive\n")
		
		exit()
		
	elif age<=0:
		
		print("You are not born yet!!")
		
		exit()
		
	else:
		
		birth_year=c_y-age
		
l=100-age
		
print(f"You will be 100 yr old in {c_y+l}")
		
	
	
print("Do you want to check your age in particular yr??\n")

i=input("Enter [y/n]")

if i=="y":
		
	try:
		p_y=int(input("Enter year\n\n"))
		
	except:
	
		print("Wrong Input!!!")
		
		exit()
		
	if p_y<c_y:
		
		print("Wrong input!!!")
		
		exit()
		
	else:
		
		print(f"You will be {p_y-birth_year}yr old in {p_y}")
		
elif i=="n":
	
	print("Okay!!!")
	
else:
	print("Wrong input!!")