
#Class
class Person:
	
	def __init__(self,fname,lname):
		
		self.fname=fname
		
		self.lname=lname
	
	def func(self):
		pass
	@property
	def name(self):
		
		return f"{self.fname} {self.lname}"
		
	@name.setter
	def name(self,string):
		
		self.fname=string.split(" ")[0]
		
		self.lname=string.split(" ")[1]
		
	@name.deleter
	def name(self):
		
		self.fname=None
		
		self.lname=None
		
a=Person("Ankit","Singh")



#Function
def inspectobject(obj):
	
	"""This function net argument obj and then it will print:-
	class of object
	manual made functions attributes
	Functions is object
	Comments in ovject
	"""
	
	#importing modules. i know importing module in function is not good practice but I am doing it one time only-
	
	import inspect
	
	
	print(f"Details about object\n")
	
	
	#id Type and dir
	
	print(f"id of object {id(obj)}\n")
	
	print(f"type of object {type(obj)}\n")
	
	print(f"dir of object {dir(obj)}")
	
	print(f"\n Class of object\n")
	
	
	
	#Class
	
	class_of_object=inspect.getmembers(obj,inspect.isclass)
	
	print(class_of_object)
	
	
	
	#Docstring
	
	print("\nDocstring of class\n")
	
	docstring=inspect.getdoc(obj)
	
	print(docstring)
	
	
	
	
	#Attributes and functions
	
	print(f"\n Made Attributes and functions in class, Not builtin\n")
	
	attributes=inspect.getmembers(a)
	
	for first,second in attributes:
		
		if first.startswith("__"):
			
			continue
		
		else:
		
			print(f"{first}  {second}")
		
		
		
		
	#Functions
	
	print(f"\n Functions in class\n")
	
	functions=inspect.getmembers(a,inspect.ismethod)
	
	
	for func_name,func_location in functions:
		
		print(f"{func_name} at {func_location}")
		
		
	#Comments
		
	print(f"Comments in class")
		
	comments=inspect.getcomments(obj)
	
	print(comments)
	
	
#Testing
	
inspectobject(a)

a.__dict__