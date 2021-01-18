class Animals:
	
	human_friendly=1#out of 100
	
	dangerous_to_human=10#out of 100
	
	mind_capability=13#out of 100
	
	
	def about(self):
		
		print("About\n")
		
		print(f"Name is {self.name}\n\n")
		
		print("Specifications\n")
		
		print(f"Human friendly:- {self.human_friendly} out of 100")
		
		print(f"Dangerous to Human:- {self.dangerous_to_human} out of 100")
		
		print(f"Mind Capability :-{self.mind_capability} out of 100")

		
	def __init__(self,name,species,location):
		
		self.name=name
		
		self.species=species
		
		self.location=location
		

cat=Animals("Cat","Cat","Mostly found in Asia South Pacific")

#cat.about()


class Dog(Animals):
	
	human_friendly=78#out of 100
	
	dangerous_to_human=0.81#out of 100
	
	mind_capability=81#out of 100
	
	cute=90 #out of 100
	
	def about(self):
		
		super().about()
		
		print(f"Cuteness :- {self.cute} out of 100")
		
		print(f"\nOwner name:- {self.owner}")
		
	def __init__(self,name,species,location,owner):
		
		super().__init__(name,species,location)
		
		self.owner=owner
		
		
		

tom=Dog("Tom","Dog","India","Ankit")
	

tom.about()