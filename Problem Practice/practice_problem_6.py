import random

try:
	
	a=int(input("Enter minimum no.\n"))
	b=int(input("Enter maximum no.\n"))
	
except:
	
	print("Wrong input!!!\n")
	
	exit()

win=random.randint(a,b)

t1=0

t2=0

while True:
	
	t1+=1
	
	print(f"Player 1 Guess a number between {a} and {b}\n")
	
	try:
		g=int(input())
	
	except:
	
		print("Wrong input!!!\n")
		
		continue
		
	
	if g>win:
		
		print(f"Wrong guess!! Try to guess a smaller no than {g}\n")
		
	elif g<win:
		
		print(f"Wrong guess!! Try to guess a greater no than {g}\n")
		
	else:
		
		print(f"Right guess You guessed in {t1} trails\n")
		
		break
		
	

while True:
	
	t2+=1
	
	print(f"Player 2 Guess a number between {a} and {b}\n")
	
	try:
		g=int(input())
	
	except:
	
		print("Wrong input!!!\n")
		
		continue
		
	
	if g>win:
		
		print(f"Wrong guess!! Try to guess a smaller no than {g}\n")
		
	elif g<win:
		
		print(f"Wrong guess!! Try to guess a greater no than {g}\n")
		
	else:
		
		print(f"Right guess You guessed in {t2} trails\n")
		
		break
		
		
if t1<t2:
		
	print("Player 1 wins!!!\n")
	
	
elif t1>t2:
		
	print("Player 2 wins!!!\n")
	
	
else:
	print("Draw")
	
	
		
	