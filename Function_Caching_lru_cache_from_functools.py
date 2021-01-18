import time

from functools import lru_cache


@lru_cache
def some_time(n):
	
	time.sleep(n)
		
	return "Function executed\n"

for i in range(2):
	
	a=some_time(3)
	
	print(a)
	

@lru_cache(maxsize=0)#I am using maxsize 0 just for fun using maxsize 0 is just a stupidity
def taking_time(n):
	time.sleep(n)
	return "Function executed"
	
for i in range(5):
	a=taking_time(5)
	print(a)


#Quiz project




if __name__=="__main__":
	
	print("Enter maximam size for lru cache limit\n")
	
	while True:
		
		try:
		
			max_size=int(input())
			print()
			break
			
		except:
			
			print("Please Enter corect no.\n")
	
	
	#Function
	
	@lru_cache(maxsize=max_size)
	def I_am_lazy_function_I_will_take_time(n):
	
		time.sleep(n)
	
	
	print("Enter time You want to run funtion\n")
	
	
	while True:
		
		try:
		
			times=int(input())
			print()
			break
			
		except:
			
			print("Please Enter corect no.\n")
	
	
			
	for i in range(times):
		
		print("Enter Time to wait now in seconds\n")
		
		while True:
		
			try:
			
				wait=int(input())
				print()
				break
				
			except:
				
				print("Please Enter corect no.\n")
		
		
		I_am_lazy_function_I_will_take_time(wait)
		
		print(f"Function executed Did this took {wait} seconds?? If yes then next it won't take because I stored it as cache memory If no then The function is executed on old cache\n")
		
		
		
#A simple real implementation of this function or decorator



from functools import lru_cache

@lru_cache
def square(n):
	l=[]
	
	for i in range(1,n+1):
		
		l.append(i**2)
		
	return sum(l)
		
a=square(10000000)
print(a)	
input("Press Enter")
a=square(10000000)
print(a)
input("Press Enter")
a=square(2000000)
print(a)

		
		
		
		