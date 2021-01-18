
# Importing modules

import datetime



class Library:
	
	def __init__(self,list_of_books,library_name):
		
		"""Init function this function will get two input list of books available in library and library name"""
		
		self.list_of_books=list_of_books
		
		self.library_name=library_name
		
		
	@property
	def available_books(self):
		
		
		available_books=self.list_of_books

		
		
		with open("lend_data.txt") as lend_file_data:
			
			data_of_file=lend_file_data.readlines()
			
			
			for each_row in data_of_file:
				
				each_book=each_row.split("-")[0]
				
				
				available_books.remove(each_book)
					
		
		return available_books
				
				

	def display_book(self):
		
		"""This function will display books available in Library"""
		
		print(f"Books avaliable in {self.library_name}:-\n")
		
		for no,each_book in enumerate(self.list_of_books,1):
			
			print(f"{no}. {each_book}")
			
		print(f"\nOnly {len(self.list_of_books)} books available in {self.library_name}\n\n")
			
			
			
	def get_add_book_input(self):
		
		"""This function will get the input of book name from user"""
		
		print("Enter Book name You are donating\n")
		
		add_book_name=input()
		
		print()
		
		
		return add_book_name
		
		
			
	def add_book(self):
			
		"""This function will add new book in list of books"""
			
		self.add_book_name=self.get_add_book_input()
		
		self.list_of_books.append(self.add_book_name)
		
		print("Thank You for giving book\n")
		
##### Lend book Functions ####

	
	@staticmethod
	def return_book_date():
		
		now_time=datetime.datetime.now()+datetime.timedelta(days=7)
	
		return now_time.strftime("%d/%m/%Y")
		
		
	@staticmethod
	def get_data_of_lend_data():
		
		list_book_customer=[]
		dictionary_book_name_customer= {}
				
		
		with open("lend_data.txt",) as lend_data_file:
			
			
			data_in_list=lend_data_file.readlines()
			
			
		for each in data_in_list:
		
			list_book_customer.append(each.split("-"))
	
			
		
		for each_book,each_customer in list_book_customer:
			
			dictionary_book_name_customer [each_book]=each_customer
			
		
		return dictionary_book_name_customer
			
			

		
	@staticmethod
	def valid_no_input(str_number,no_of_last_book):
		
		"""This function will get the number as argument and check wheter the number is valid number(able to convert to integer) or not"""
		
		try:
			
			number=int(str_number)
			
			
			if number>=1 and number<=no_of_last_book:
				
				return True
				
			else:
				
				return False
			
		except:
			
			return False
			
			

	def customer_email(self,customer_name):
			
		return f"{customer_name}@{self.library_name}.com"
			
	def get_user_details(self):
		
		"""This function will get the name of customer as input"""
		
		print("Enter Your name\n")
		
		name=input()
		
		print()
		
		
		return name
		

	def check_avaibility_of_book(self,book_name):
		
		"""This will check the availability of book while user is lending it"""
		
		if book_name in self.available_books:
			
			return True
		
		else:
			
			return False
		
	@staticmethod
	def add_new_lend_data_in_file(book,customer):
		
		new_data=f"{customer}-{book}\n"
		
		with open("lend_data.txt","a") as lend_data_file:
		
			lend_data_file.write(new_data)
			
			
			
			
		
		
		
	def input_lend_book(self):
		
		for no,each_book in enumerate(self.list_of_books,1):
			
			print(f"Enter {no} to buy {each_book}\n")
			
	
		
		
		
		while True:#Wrong input handling
		
			input_book_no=input()
			
			print()
			
			if self.valid_no_input(input_book_no,len(self.list_of_books)):
				
				self.book_lend_no=int(input_book_no)
				
				
				break
				
			else:
				
				print("Please Enter Correct no.\n")
				
		
			
		return self.list_of_books[self.book_lend_no-1]
		
		
		
		
	def lend_book(self):
		

		self.lend_book_name=self.input_lend_book()
		
		if self.check_avaibility_of_book(self.lend_book_name):
				
			
			self.customer_name=self.get_user_details()
		
			self.add_new_lend_data_in_file(self.customer_name,self.lend_book_name)
			
			print(f"You need to return book before {self.return_book_date()}\n")
			
		else:
			
			print("Sorry, That book is not avaliable\n")
			dictionary_of_lend_book_and_customer=self.get_data_of_lend_data()
			
			
			
			print(f"If you have urgent work then contact to '{self.customer_email(dictionary_of_lend_book_and_customer.get(self.lend_book_name))}' who lends this book\n")
			
			
##### Return book Functions #####


	def get_details_as_input(self):
			
		print("Enter Your name\n")
		
		self.customer_name_input=input().lower()
		
		print()
		
		print("Enter name of book You are giving\n")
		
		
		self.book_name_input=input().lower()
		
		print()
		
		
	
	@staticmethod
	def delete_returned_book(book_name,customer_name):
			
		with open("lend_data.txt") as lend_data_file:
			
			old_lend_data=lend_data_file.readlines()
			
		for each_row in old_lend_data:
			
			each_book=each_row.split("-")[0]
			
			customer_name_data= each_row.split("-")[1]
			
			
			if each_book==book_name and customer_name_data==customer_name:
				
				old_lend_data.remove(f"{book_name}-{customer_name}")
				
		
		
		with open("lend_data.txt","w") as lend_data_file:
			
			for each_row in old_lend_data:
				
				lend_data_file.write(each_row)
			
			
			
	def return_book(self):
			
		self.get_details_as_input()
		
	
		
		self.delete_returned_book(self.book_name_input,self.customer_name_input)
		
		
	
			
			
####### MAIN FUNCTION ######
			
	def show(self):
		
		print("Enter 1 to see books available in library\n")
		
		
		print("Enter 2 to donate or add book\n")
		
		print("Enter 3 to lend book available in library\n")
		
		print("Enter 4 to return book\n")
		
		
	def get_choice(self):
		
		while True:
		
			choice=input()
			
			print()
			
			
			try:
				
				choice=int(choice)
				
				if choice>=1 and choice<=4:
					
					break
					
				else:
					
					print("Please Enter correct choice\n")
					
			except:
				
				print("Please Enter correct choice\n")
				
				continue
				
				
		if choice==1:
			
			self.display_book()
			
		elif choice==2:
			
			self.add_book()
			
			
		elif choice==3:
			
			self.lend_book()
			
			
		elif choice==4:
			
			self.return_book()
			
			
	@staticmethod		
	def again_show_options():
			
			
		while True:
				
			print("Do you want to see options again [y/n]\n")
			
			again=input().lower()
			
			print()
			
			
			if again=="y":
				
				return True
				
				break
				
			elif again=="n":
				
				print("Okay bye bye\n")
				
				break
				
			else:
				
				print("Please Enter correct input\n")
		
		
			
	def main(self):
			
		print(f"Welcome to {self.library_name}\n")
		
		while True:
			
			
			self.show()
		
			self.get_choice()
			
			if self.again_show_options():
				
				continue
				
			else:
				
				break
		


a=Library(["2","3","44","5","56","6","6"],"Harry Library")
a.main()
		