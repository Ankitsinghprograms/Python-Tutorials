import time

class Electronic_Device:
	
	average_price="₹1000"
	
	shops="1000 shops"
	
	big_shops_name=["All in one Electronic shop","Best Electroic Shop","Best Electronic Shop Ever"]
	
	def shops(self):
		return self.big_shops_name
		
class Pocket_Device(Electronic_Device):
	
	average_price="₹2500"
	
	big_companies=["Apple","Samsung","ASUS","Boot"]
	
	def companies(self):
		
		return self.big_companies
		
		
class Phone(Pocket_Device):
		
		average_price="₹5000"
		
		avaliable_software=["Andriod","OS","Mac","Linux"]
		
		new_phones=["Redmi 8 A Dual","Samsung Galaxy 4","IPhone 11"]
		
		
		def details(self):
			
			return f"Average Price of phone {self.average_price} New phone Launched in November 2020 {self.new_phones} Best softwares {self.avaliable_software}"
			
			
coustmer_want_to_Buy=Phone()

print("Hii I am Phone Buying Helper Bot I will save our money and suggest you to buy best phone\n")

print("I am searching for phone just wait\n")


#Just For Fun
for i in range(4):
	
	print(".")
	
	time.sleep(0.5)
	


print("\n\n Here what I found\n")

print(f"{coustmer_want_to_Buy.details()} Big Companies  {coustmer_want_to_Buy.companies()} Shops Near You {coustmer_want_to_Buy.shops()}")
	
	