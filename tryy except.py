print("Enter a number\n")
while True:
	try:
		a=int(input("Enter First no.\n"))
		b=int(input("Enter Second no.\n"))
		c=a+b
		print(c,"\n")
	except Exception as d:
		print("Please Only enter any integer value\n")
		print(d)