print("Driving License Egibility\n")
print("What is Your age\n")
age=int(input())
print("\n")
if age>110:
	print("Enter Correct Age")
elif age>80:
	print("Sorry You are So Old So You can't Drive\n")
elif age>18:
	print("Yes You are Eligible to Drive\n")
elif age<0:
	print("Enter correct age\n")	
elif age<18:
	print("Sorry You are Not eligible to Drive\n")
else:
	print("We will think About You\n")