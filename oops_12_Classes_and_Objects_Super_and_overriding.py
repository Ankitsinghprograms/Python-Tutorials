class Languages():
	def __init__(self,name,people,country):
		self.name=name
		self.people=people
		self.country=country

class Programming_Languages(Languages):
	
	def __init__(self,name,people,country,softwares):
		
		super().__init__(name,people,country)
		
		self.softwares=softwares

		
python=Programming_Languages("Python","1 million","Worldwide","Andriod,Mac,Linux,Windows,etc..")

print(python.name) #Getting this from Class Languages __init__ or constructor Function
		
		
		
class Languages():
	def __init__(self,name,people,country):
		self.name=name
		self.people=people
		self.country=country
		self.detail="Spoking Language"
		
class Programming_Languages(Languages):
	
	def __init__(self,name,people,country,softwares):
		
		super().__init__(name,people,country)
		
		self.softwares=softwares
		
		self.detail="Computer Language High level Programming Language"#Changing Detail variable after calling super().__init__() #So now detail variable is changed to Computer Language High level Programming Language
		
		
python=Programming_Languages("Python","1 million","Worldwide","Andriod,Mac,Linux,Windows,etc..")

print(python.detail)#Gettimg this from Class Programming_Languages



class Languages():
	def __init__(self,name,people,country):
		self.name=name
		self.people=people
		self.country=country
		self.detail="Spoking Language"
		
class Programming_Languages(Languages):
	
	def __init__(self,name,people,country,softwares):
		
		self.softwares=softwares
		
		self.detail="Computer Language High level Programming Language"
		
		super().__init__(name,people,country)#Calling Super Function after changing deatil Variable so now detail variable is changed to Spoking Language
		
		
python=Programming_Languages("Python","1 million","Worldwide","Andriod,Mac,Linux,Windows,etc..")

print(python.detail)#Gettimg this from Class Languages
		