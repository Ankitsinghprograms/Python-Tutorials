class School:
	standard=12
	
	def __init__(self,name,city,grade):
		self.name=name
		self.city=city
		self.grade=grade
		
	def details(self):
		return f"{self.name} {self.city} {self.grade} {self.standard}"
	
	@classmethod
	def change_class(cls,new_class):
		cls.standard=new_class
		
		
print(f"Before changing the class variable {School.standard}\n")
	
a=School("Camford Public School","Patna Bihar","C")

#Here I changed intance varible by @classmethod
a.change_class(10)

print(a.details())
print()

#Here we only changed intance varibale but by using class method class method is also has been changed
print(f"Class variable after changing instance variable by class method {School.standard}\n")

b=School("Vanasthali Gayanpeth","Patna Bithar","B")

print(f"New object varible is also has been changed {b.standard}\n")




	