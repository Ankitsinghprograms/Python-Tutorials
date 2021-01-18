try:
	import search_web
	
except:

	raise Exception("Unable to import search-web module \n\
Please download it via 'pip install search-web'")


def divide(a,b):
	
	if b==0:
		
		raise ZeroDivisionError("Couldn't Divide by 0")
		
	return a/b

b=divide(0,2)
print(b)



name=input("Enter Your name\n\n")

if name=="":
	
	raise EOFError("Please enter your name")