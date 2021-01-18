class Players:
	
	var=1
	
	def __init__(self,name,age,fitness_level):
		
		self.name=name
		
		self.age=age
		
		self.fitness=fitness_level
		
	def details(self):
		
		return f"Name is {self.name} {self.age} years old and Fitness Level {self.fitness}"
		
class Cricketer:
	
	var=2
	
	def __init__(self,name,age,fitness_level,country,role):
		
		self.name=name
		
		self.age=age
		
		self.fitness=fitness_level
		
		self.country=country
		
		self.role=role
		
	def details(self):
		
		return f"Name is {self.name} {self.age} years old Fitness Level {self.fitness} Representing Country {self.country} Role is {self.role}"
		
#class Batsman(Players,Cricketer): #Here Order also matters Players is in first So Its first take Players __init__ function,method and variables then take Cricketer __init__ function,method and variable
#	
#	var=3



#virat=Batsman("Virat Kohli",23,"A+")

#print(f"I am printing details from details function from Players Method {virat.details()}")


#class Batsman(Cricketer,Players): #Here Order also matters Cricketer is in first So Its first take Cricketer __init__ function,method and variables then take Players __init__ function,method and variable
#	
#	var=3



#virat=Batsman("Virat Kohli",23,"A+","India","Batsman")

#print(f"I am printing details from details function from Cricketer Method {virat.details()}")


#class Batsman(Players,Cricketer): #Here Order also matters Players is in first So Its first take Players __init__ function,method and variables then take Cricketer __init__ function,method and variable
#	
#	var=3



#virat=Batsman("Virat Kohli",23,"A+")

#print(f"I am printing var variable from Batsman Classes There are also Variable var in Players and Cricketer Classes but it's giving privority to Batsman Class '{virat.var}'")


class Batsman(Players,Cricketer): #Here Order also matters Players is in first So Its first take Players __init__ function,method and variables then take Cricketer __init__ function,method and variable


virat=Batsman("Virat Kohli",23,"A+")

print(f"I am printing var variable from Players Class Due to Order There are also Variable var in  Cricketer Class but it's giving privority to Player Class Due to Order {virat.var}")


	
	