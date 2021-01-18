l=list(input("Enter numbers seprated by space\n\n").split())

#method 1

m1=sorted(l,reverse=True)

print(m1)

#method 2
m2=l[::-1]

print(m2)

#method 3

m3=[]

for each in l:
	
	m3.insert(0,each)
	
print(m3)


if m1==m2 and m2==m3 and m3==m1:
	
	print("All methods are same\n")
	
else:
	
	print("All methods aren't same\n")