class Person:
	
	def __init__(self,fname,lname):
		
		self.fname=fname
		
		self.lname=lname
		
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

#print(a.name)

a.name="Sumit Singh"

#print(a.fname)

del a.name
print(a.name)

		
	