
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
time_now = now.strftime("%d/%m/%Y %H:%M:%S")



while True:
	print("\nEnter Your name\n")
	
	name=input()
	
	name_lower=name.lower()
	
	if name_lower=="ankit":
		print("\n",name,"\n")
		
		print("Enter 1 to add\n")
		print("Enter 2 to see progress\n")
		type=input()
		
		if type=="1":
			print("\nEnter 1 for Exercise\n")
			print("Enter 2 for Diet\n")
			
			add_type=input()
			
			if add_type=="1":
				ankit_exercise= open("Ankit exercise.txt","a")
				print("\nEnter exercise name\n")
				add_exercise=input()
				
				
				ankit_exercise.write("[")
				ankit_exercise.write(time_now)
				ankit_exercise.write("] ")
				ankit_exercise.write(add_exercise)
				ankit_exercise.write("\n")
				
				print("\n Sucessfully added\n")
				ankit_exercise.close()
				
			elif add_type=="2":
				ankit_diet=open("Ankit diet.txt","a")

				print("\nEnter Diet name\n")
				
				
				add_diet=input()
						
				
				ankit_diet.write("[")
				ankit_diet.write(time_now)
				ankit_diet.write("] ")
				ankit_diet.write(add_diet)
				ankit_diet.write("\n")
				
				print("\n Sucessfully added\n")
				ankit_diet.close()
				
			else:
				print("\nPlease Enter right key\n")
			
		elif type=="2":
			print("\nEnter 1 to see progress of Exercise\n")
			print("Enter 2 to see progress of Diet\n")
			print("Enter 3 to see progress of Both Exercise and Diet\n")
			
			see_type=input()
			print("\n")
			
			if see_type=="1":
				ankit_exercise =open("Ankit exercise.txt","r")

				print("Exercise progress\n")
				print(ankit_exercise.read())
				ankit_exercise.close()
			
			elif see_type=="2":
				ankit_diet=open("Ankit diet.txt","r")

				print("Diet progress\n")
				print(ankit_diet.read())
				ankit_diet.close()
			
			elif see_type=="3":
				ankit_exercise =open("Ankit exercise.txt","r")

			
				print("Exercise progress\n")
				print(ankit_exercise.read())
				ankit_exercise.close()
				ankit_diet=open("Ankit diet.txt","r")

				print("Diet progress\n")
				print(ankit_diet.read())
				ankit_diet.close()
			
			
			else:
				print("\n Please Enter right key\n")
		
		break
		
		
	elif name_lower=="sumit":
		print("\n",name,"\n")
		
		
		print("Enter 1 to add\n")
		print("Enter 2 to see progress\n")
		type=input()
		
		if type=="1":
			print("\nEnter 1 for Exercise\n")
			print("Enter 2 for Diet\n")
			
			add_type=input()
			
			if add_type=="1":
				sumit_exercise =open("Sumit exercise.txt","a")
				print("\nEnter exercise name\n")
				add_exercise=input()
				
				
				sumit_exercise.write("[")
				sumit_exercise. write(time_now)
				sumit_exercise.write("] ")
				sumit_exercise.write(add_exercise)
				sumit_exercise.write("\n")
				
				print("\n Sucessfully added\n")
				sumit_exercise.close()
				
			elif add_type=="2":
				sumit_diet =open("Sumit diet.txt","a")
				
				print("\nEnter Diet name\n")
				
				
				add_diet=input()
							
				sumit_diet.write("[")
				sumit_diet.write(time_now)
				sumit_diet.write("] ")
				sumit_diet.write(add_diet)
				sumit_diet.write("\n")
				
				print("\n Sucessfully added\n")
				sumit_diet.close()
				
			else:
				print("\nPlease Enter right key\n")
			
		elif type=="2":
			print("\nEnter 1 to see progress of Exercise\n")
			print("Enter 2 to see progress of Diet\n")
			print("Enter 3 to see progress of Both Exercise and Diet\n")
			
			see_type=input()
			print("\n")
			
			if see_type=="1":
				sumit_exercise =open("Sumit exercise.txt","r")
				print("Exercise progress\n")
				print(sumit_exercise.read())
				sumit_exercise.close()
			
			elif see_type=="2":
				sumit_diet=open ("Sumit diet.txt","r")
				print("Diet progress\n")
				print(sumit.read())
				sumit_diet.close()
			
			elif see_type=="3":
				sumit_exercise=open ("Sumit exercise.txt","r")
			
				print("Exercise progress\n")
				print(sumit_exercise.read())
				sumit_exercise.close()
				
				print("Diet progress\n")
				sumit_diet= open("Sumit diet.txt","r")
				print(sumit_diet.read())
				sumit_diet.close()
			
			
			else:
				print("\n Please Enter right key\n")
			
		else:
			print("\nPlease Enter Right key\n")
	
		break
		
	elif name_lower=="sangita":
		print("\n",name,"\n")
		
		print("Enter 1 to add\n")
		print("Enter 2 to see progress\n")
		type=input()
		
		if type=="1":
			print("\nEnter 1 for Exercise\n")
			print("Enter 2 for Diet\n")
			
			add_type=input()
			
			if add_type=="1":
				sangita_exercise= open("Sangita exercise.txt","a")
				print("\nEnter exercise name\n")
				add_exercise=input()
				
				
				sangita_exercise.write("[")
				sangita_exercise.write(time_now)
				sangita_exercise.write("] ")
				sangita_exercise.write(add_exercise)
				sangita_exercise.write("\n")
				
				print("\n Sucessfully added\n")
				sangita_exercise.close()
				
			elif add_type=="2":
				sangita_diet= open("Sangita diet.txt","a")
				print("\nEnter Diet name\n")
				
				
				add_diet=input()
							
				sangita_diet.write("[")
				sangita_diet.write(time_now)
				sangita_diet.write("] ")
				sangita_diet.write(add_diet)
				sangita_diet.write("\n")
				
				print("\n Sucessfully added\n")
				sangita_diet.close()
				
			else:
				print("\nPlease Enter right key\n")
			
		elif type=="2":
			print("\nEnter 1 to see progress of Exercise\n")
			print("Enter 2 to see progress of Diet\n")
			print("Enter 3 to see progress of Both Exercise and Diet\n")
			
			see_type=input()
			print("\n")
			
			if see_type=="1":
				sangita_exercise= open("Sangita exercise.txt","r")
				print("Exercise progress\n")
				print(sangita_exercise.read())
				sangita_exercise.close()
			
			elif see_type=="2":
				sangita_diet= open("Sangita diet.txt","r")
				print("Diet progress\n")
				print(sangita_diet.read())
				sangita_diet.close()
			
			elif see_type=="3":
				sangita_exercise= open("Sangita exercise.txt","r")
			
				print("Exercise progress\n")
				print(sangita_exercise.read())
				sangita_exercise.close()
				
				sangita_diet= open("Sangita diet.txt","r")
				print("Diet progress\n")
				print(sangita_diet.read())
				sangita_diet.close()
			
			
			else:
				print("\n Please Enter right key\n")
			
		else:
			print("\nPlease Enter Right key\n")
		
		break
	
	else:
		print("\nPlease Enter Correct name\n")
		
