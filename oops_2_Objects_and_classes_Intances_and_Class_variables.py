class Students:
	
	percentage=0 #Class varibales
	
harry=Students()

harry.name="Harry"

print(harry.name,harry.percentage)

print(harry.percentage) #Object

print(Students.percentage) #Class


#Changing Class Variables

#Changing Object variable

ankit=Students()

ankit.percentage=100

print(ankit.percentage)


#Changing Class variable

Students.percentage=100

print(Students.percentage)

print(harry.percentage)

print(ankit.percentage)