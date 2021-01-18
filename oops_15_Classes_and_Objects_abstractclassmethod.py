from abc import ABC,abstractmethod

class Phone(ABC):
	
	def __init__(self,name,model,software,company,year):
		
		self.name=name
		
		self.model=model
		
		self.software=software
		
		self.company=company
		
		self.year=year
	
	@abstractmethod
	def details(self):
		return f"Phone name {self.name} phone model {self.model} phone Software {self.software} Phone built by {self.company} Phone built in {self.year}"
		

#print("\nError because Phone class is forcing Andriod phone class to make function 'details' but andriod phone haven't made it\n")

#class Andriod_Phone(Phone):
#		
#		pass 
#		

#redmi=Andriod_Phone("Redmi 8 A Dual",'Redmi Mi',"Andriod 10","Xiaomi",2020)


class Andriod_Phone(Phone):
		
	def details(self):
		return f"Phone name {self.name} phone model {self.model} phone Software Andriod 9 or higher(mostly 10.0.1.2) Phone built by {self.company} Phone built in {self.year}"


redmi=Andriod_Phone("Redmi 8 A Dual",'Redmi Mi',"Andriod 10","Xiaomi",2020)


print(redmi.details)