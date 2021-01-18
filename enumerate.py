l=["orange","mango","banana","cake","laptop","choclate"]

#enumerate function makes a new no As we defined no as variable no but we can use anything instead of this
#no starts from 0
for no,i in enumerate(l):
	if no%2==0:
		print(f"You need To buy {i}")
		
print("\n'enumerate' Function makes everything easy\n")

#We can Define no

for no,k in enumerate(l,2):#here me defined no as 2
	print(no,k)
	
