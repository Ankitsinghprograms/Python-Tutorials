
# Syntax Changes
#print function
#xrange ----> range
# Exception as


#print function changes


#Python 2
#print "Hii"

#Python 3

#print("Hii")



#Division operator changes

#Python 2

#print 7/2 ----> int

#print 7.0/2 -----> float

#print -7/2 -----> Real result -3.5 then round to -4(int)



#Python 3
#print(7/3) # -----> float

#print(7.0/3) # ------> float

#print(7.0//3) # //= Base operator

print(-7//2) #Real result -3.5 then round to -4(int)





#Python 2 Unicode and String are different

a=u"Hii"
b="Hii"
print type(a),type(a)

#Python 3 Unicode and string are same


a=u"Hii"
b="Hii"
print(type(a),type(a))



#Python 2 bytes and string are same

a=b"Hii"
b="Hii"
print type(a),type(a)



#Python 3 bytes and string are different

a=b"Hii"
b="Hii"
print(type(a),type(a))


#Python 2 xrange

for i in xrange(5):
	print(i)


#Python 3 xrange is changed to range
for i in range(5):
	print(i)
	
	
	
#Error handling


#Python 2 we use , instead of as

try:
	int("sh")
	
except ValueError,e:
	print e
	
#Python 3 We use e

try:
	int("sh")
	
except ValueError as e:
	
	print(e)
	
	
	
# To change any Code From Python 2 to Python 3

pip install 2to3


2to3 filename -w


#### Easy ####


# To use python 3 Functions in python 2


#import __future__ #module

