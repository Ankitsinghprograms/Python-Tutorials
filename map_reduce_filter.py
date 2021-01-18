
#---------MAP-----------

#l=[3,3,4,5,6,6,5,7,4,7,5,6,4,5,4,4,4444,4,4,4,54554,5,5]

#n=list(map(lambda x:x**2,l))

#print(n)

#Important It also used in making alogrithms

#l=[3,3,4,5,6,6,5,7,4,7,5,6,4,5,4,4,4444,4,4,4,54554,5,5]


#def sq(a):
#	return a**2
#def cube(a):
#	return a**3
#	
#func=[sq,cube]
#	
#for i in l:
#	n=list(map(lambda x:x(i),func))
#	print(n)


#------------Filter-------------

#l=[3,3,4,5,6,6,5,7,4,7,5,6,4,5,4,4,4444,4,4,4,54554,5,5]

#def greater_5(num):
#	return num>5

#a=list(filter(greater_5,l))

#print(a)

#a=["a","b","d","g","e","a","o","u","i","j","n","m","f","u","i","o"]

#def vowels(n):
#	vowel=["a","e","i","o","u"]
#	
#	if n in vowel:
#		return True
#	else:
#		return False

#l=list(filter(vowels,a))
#print(l)


#--------Reduce-----

#from functools import reduce

#l=[74,64,554,54,54,4,3,3,5,3,4,3,34,3,]


#a=reduce(lambda x,y:x+y,l) #Sum of all numbers in l

#print(a)
