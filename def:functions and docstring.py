	
print("Percentage Finder\n")
print("Enter total marks you obtained\n")
marks=int(input())
print("\nEnter Total marks of exam\n")
total=int(input())
print("\n")

def percent():
	"""This is used to find percentage by getting full marks
	Make this function to be applicable to find pecentage of every subject"""
	percentage=(marks/total)*100
	print("Your percentage is",percentage)
	return percentage
	


percent()
print(percent.__doc__)