def gen(n):
	for i in range(n):
		yield i
		
a=gen(10)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

def fact(n):
	sum=1
	
	for i in range(1,n+1):
		sum*=i
		yield sum
		
a=fact(10)

for each in a:
	print(each)
	
	
def fib(n):
	
	first=1
	second=1
	
	for i in range(n):
		
		yield first
		
		first,second=second,first+second


		
b=fib(5)
for first in b:
	print(f"First no: {first}")
	
d={1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10}

itr=iter(d)
print(itr)
for each in itr:
	print(each)
	
	
	
class A:
	
	def __init__(self,max,num=0):
		
		self.num=num
		
		self.max=max
		
		
	def __iter__(self):
		return self
		
	def __next__(self):
		
		if self.num<self.max:
				
			self.num+=1

			return self.num
		else:
			
			raise StopIteration
			


a=A(3)
b=iter(a)

print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())