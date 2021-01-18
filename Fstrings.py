import time


a=1
b=2
#print(time.perf_counter())
#string formatting
#print("Hii %s"%a)
#print("hii %s %s"%(a,b))
#print(time.perf_counter())

#Formatting

#c="hello {} {}"
#d=c.format(a,b)
#print(d)
#print(time.perf_counter())

#Fstring

d=time.perf_counter()
print(time.perf_counter())
print(f"Hello {a} {b}")
c=time.perf_counter()
print(d-c) #time taken to execite the code
print(time.perf_counter())