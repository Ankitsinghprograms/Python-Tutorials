class Apps():
	
	def __init__(self,name,users,rating):
	
		self.name=name
	
		self.users=users
	
		self.rating=rating
		
	def details(self):
		
		return self.name
	
	@staticmethod
	def availabe():
		return "Availabe at Playstore and Ios Store"
	

facebook=Apps("Facebook","500 Miliion", "4.7 Star")


class Messenging_Apps(Apps):
	
	def __init__(self,name,users,rating,security):
	
		self.name=name
	
		self.users=users
	
		self.rating=rating
	
		self.secure=security
		
whatsapp=Messenging_Apps("Whatsapp","600 million","4.9 Star","Most secured")

print(whatsapp.availabe())