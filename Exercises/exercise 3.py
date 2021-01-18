won=17
print("Guess the no. game\n")
n=0
guess=9
guesses=0
while True:
	guess=guess-1
	guesses=guesses+1
	
	print("Enter A No. between 1 to 20\n")
	
	inpu=int(input())
	print("\n")
	
	if inpu==won:
		print("Horray You won tbe game\n")
		print("You won in ",guesses," guesses\n")
		break
		
	elif guess==0:
		print("Game Over\n")
		break
		
	elif inpu>20 or inpu<1:
		print("Enter A no. between 1 to 20\n")
	elif inpu>won:
		print("You guessed larger no. Try to guess A no. smaller than ",inpu,"\n")
	elif inpu<won:
		print("You guessed samller no. Try to guess A no. larger than ",inpu,"\n")
	else:
		print("Enter A no. between 1 to 20\n")
		
	print("Only ",guess," guesses left\n")

	