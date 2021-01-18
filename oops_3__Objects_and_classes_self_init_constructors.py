#class Teachers:
#	
#	def details(self):
#		
#		return f"Teacher name is {self.name} {self.name} has {self.no_of_leaves} of leaves {self.name} is Class Teacher of class {self.class_teacher} {self.name} teaches Subject {self.subject}"
#		
#santosh=Teachers()

#santosh.name="Santosh Kumar"

#santosh.no_of_leaves=20

#santosh.class_teacher=8

#santosh.subject="S.st"

#print(santosh.details())


#__init__

class Teachers:

	def __init__(self,get_name,get_class_teacher,get_subject):
		
		self.name=get_name
		
		self.class_teacher=get_class_teacher
		
		self.subject=get_subject
		
	def details(self):
		
		
		return f"Teacher name is {self.name} {self.name} is Class Teacher of class {self.class_teacher} {self.name} teaches Subject {self.subject}"
		
	
Santosh=Teachers("Santosh Kumar",8,"S.st")


print(Santosh.details())