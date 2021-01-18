def greet(name):
	
	""" This will greet you
	
	____________________
	Parameters
	
	~ name:- Your name (str)
	_____________________
	
	"""
	
	print("Hello"+name)


class Prog:
	
	"""
	This is Class for programers
	
	"""
	
	def __init__(self,name,age,p_lang):
		
		"""
		__init__ function
		
		_______________
		Parameters
		_______________
		
		name:- Programmer name (str)
		
		age:- Programmer age (str)
		
		p_lang:- Programming languages Programmer know (list)
		
		"""
		
		self.name=name	
		
		self.age=age
		
		self.p_lang=p_lang
		
		print(f"Hello {self.name}")
		
		
	def details(self):
		
		"""
		
		Print details about programmer
		
		"""
		
		print(f"Name: {self.name}\
Age: {self.age}\
Programming Languages:- {self.p_lang}\n")



