#def numbers(*no):
#	for i in no:
#		print(i)
#	print(no)
#input=input()
#numbers(*input)

#def numbers(*no):
#	for i in no:
#		print(i)
#a=["hii","bye","hello","nihaho","namaste"]
#numbers(*a)


#def numbers(normal,*no):#normal argument is at first postion or you are getting error
#	for i in no:
#		print(normal,i)
#a=["Ankit","Sumit","Sangita","Sourabh","Chinmay"]
#numbers("Hii I am",*a)


def numbers(**no):
	for i,b in no.items():
		print(i,b)

a={"Ankit":"World's best programmer","Sumit":"Tense about his carrer","Sangita":" Tension ka shop","Vijay Kumar Singh":"namm bhi mat lo"}

numbers(**a)

def numbers(normal,**no):#kwrags are used after the normal and args arrguments
	for i,b in no.items():
		print(f"Ideas of persons {normal} {i} {b}")

a={"Ankit":"World's best programmer","Sumit":"Tense about his carrer","Sangita":" Tension ki shop","Vijay Kumar Singh":"namm bhi mat lo"}


numbers("hii",**a)



