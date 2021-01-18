import time
#time_1=time.asctime(time.localtime(time.time()))
#print(time_1)

#time_2=time.localtime(time.time())
#print(time_2)

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%H:%M:%S", named_tuple)

n="12:27:00"
while True:
	
	named_tuple = time.localtime() # get struct_time
	time_string = time.strftime("%H:%M:%S", named_tuple)

	if n==time_string:
		print("Yes")
	else:
		print(time_string)
		
		time.sleep(1)






#i=0
#while i<=2000:
#	print(f"Hii I am at {i}")
#	a=time.time()
#	i+=1
#	a=a*2
#	
#print(f"Through F strings {time.time()-(a/2000)}")
#compare1=time.time()-a/2000

#b=0
#while b<=2000:
#	print("Hii I am at",i)
#	d=time.time()
#	b+=1
#	d=d*2
#	
#	print("Without F strings",time.time()-(d/2000))
#compare2=time.time()-d/2000

#if compare1>compare2:
#	print(f"Fstrings are fast by {compare1-compare2}")
#else:
#	print("Fstrings are slow by",compare1-compare2)

print("Wait\n")
time.sleep(1)
print("Bye")

