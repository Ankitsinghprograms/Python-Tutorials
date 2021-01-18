file=open("files.txt","rt")
print(file.read())
for lines in file:
	print(lines)
file.close()

file1=open("file1.jpg","rb")
print(file1)
file1.close()

file=open("files.txt","rt")
for lines in file:
	print(lines)
file.close()

file=open("files.txt","rt")
print(file.readline())
print(file.readline())
file.close()


file=open("files.txt","rt")
print(file.readlines())
file.close()


