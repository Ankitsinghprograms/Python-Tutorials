class Employee:
	
	def __init__(self,emp_id,name,salary,role):
	
		self.emp_id=emp_id
	
		self.name=name
	
		self.salary=salary
	
		self.role=role
		
	def __gt__(self,other):#<
		
		if self.salary>other.salary:
			
			print(f"{self.name}'s salary is getter than {other.name}'s salary by '{self.salary-other.salary}'")
			
		else:
			
			print(f"No {self.name}'s salary is not getter than {other.name}'s salary")
			
	def __iadd__(self,add):#+=
		
		self.salary+=add
		
		print(f"{self.name}'s salaray id increased by '{add}' and now his total salary is '{self.salary}'")
		
	def __eq__(self,other):# ==
		
		if self.role.lower()==other.role.lower():
			
			print(f"Yes, '{self.name}' and '{other.name}' has same role in company. They both are '{self.role}'")
		
		else:
			
			print(f"No, '{self.name}' and '{other.name}' hasn't same role in company. '{self.name}' is '{self.role}' and '{other.name}' is '{other.role}'")

	
	def __repr__(self):
		
		return f"Employee({self.emp_id},'{self.name}',{self.salary},'{self.role}')"
		
	def __str__(self):
		
		return f"Employee ID is '{self.emp_id}' Name is '{self.name}' Salary '₹{self.salary}'/per month Role is '{self.role}' in Company"


emp1=Employee(1,"Harry",1735,"Programmer")

emp2=Employee(2,"Ankit",2000,"Programmer")


emp2==emp1
#emp2+=1000
emp2>emp1

print(emp2)

print(repr(emp1))
			
