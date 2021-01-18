class A:
 
 def about(self):
 	print("Hii I am in Class A. Let's learn Diamond shape Problem. This is gone to be fun.")

class B(A):
 	def about(self):
 		print("Hii I am in Class B. Let's learn Diamond shape Problem. This is gone to be fun.")

class C(A):

 	def about(self):
 		print("Hii I am in Class C. Let's learn Diamond shape Problem. This is gone to be fun.")

 	

class D(B,C):
	pass
#	def about(self):
	#	print("Hii I am in Class D. Let's learn Diamond shape Problem. This is gone to be fun.")


o = D()

o.about()