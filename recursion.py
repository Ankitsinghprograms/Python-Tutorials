#def fibonaci(n):
#	if n==0:
#		return 1
#	else:
#		return fibonaci(n-1)+fibonaci(n-2)
#		
#fibonaci(5)

e=0

def iterative(i):
	for d in range(i):
		global e
		e=e+1
		print(e)
iterative(5)

def factorial(z):
	y=1
	for i in range(z):
		y=y*z
		
	print(y)
	
factorial(5)
