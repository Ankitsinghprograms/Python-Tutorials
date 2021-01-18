#def a():
#	print("Hello This Decorator")
#	
#b=a

#del a

#This will run the function beacuse it made a copy of a() function to b().This will even work after deletinv old function

#b()


#We could also use any function inside function

#def sum():
#	print("I am in sum function")
#	
#def hello():
#	
#	print("Hello World, I am in hello function")

#def func(num):
#	
#	if num==0:
#		
#		return sum()
#		
#	else:
#		
#		return hello()
#		

#func(0)




#******Decorators*********


#def func(func_1):
#	
#	def inner_func():
#		
#		print("I am executing code just wait")
#		
#		func_1()
#		
#		print("I executed code")
#		
#	return inner_func
#	
#	
#		
#def func_3():
#	
#	print("Hello I am Function 3")
#	

#func_3=func(func_3)

#func_3()


#Shortform of decorators @function_name


#def func(func_1):
#	
#	def inner_func():
#		
#		print("I am executing code just wait")
#		
#		func_1()
#		
#		print("I executed code")
#		
#	return inner_func
#	

#@func
#		
#def func_3():
#	
#	print("Hello I am Function 3")

#func_3()


#Using decorators to find time of execution of any function

import time

def time_taken(function):
	
	
	time_1=time.time()
		
	print(f"\nTime before executing function {time_1}")
		
		
	function()
		
	time_2=time.time()

		
	print(f"\nTime taken to execute this code {time_2-time_1}")
		
	
	
@time_taken

def loop():
	
	n=0
	
	while n<10000:
		
		print("Hello,I am while loop")
		
		n+=1
	

