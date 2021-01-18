def add(a,b):
	print(a+b)
	

#This will print the sum also in file in which we are using this function by importing
#add(8,7)

#But IF we use If__name__=="main"
#This will no printed in all files which are importing the functions of this file

if __name__=="__main__":
	add(8,7)