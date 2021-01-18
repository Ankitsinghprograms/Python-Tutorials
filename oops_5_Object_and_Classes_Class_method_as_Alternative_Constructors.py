class Adhar_Card():
	
	nation="India"
	
	def __init__(self,adhar_no,name,age,city):
		self.adhar_no=adhar_no
		
		self.name=name
		
		self.age=age
		
		self.city=city
		
	@classmethod
	def from_dash(cls,string):
		
		#a=string.split("-")
#		
		#return cls(a[0],a[1],a[2],a[3])
#		#Another Way of this using args(*)

		return cls(*string.split("-"))
		

#first=Adhar_Card.from_dash("983537363-Ankit Singh-13-Patna Bihar")

#print(first.name)



#Real Use Of this is to get data through any txt file

with open("oops_5_Object_and_Classes_Class_method_as_Alternative_Constructors.txt") as data_from_txt_file:
	
	data=data_from_txt_file.readlines()
	
	for each_row in data:
		
		a=Adhar_Card.from_dash(each_row)
		
		print(a.name,end="\n\n")

