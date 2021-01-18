with open("more on files.txt") as f:
	print(f.read(6))
	#No need to close the file with block automatically closes the file.
f=open("more on files.txt")
print(f.tell())
print(f.read(63))
print(f.tell())
f.seek(0)
print(f.tell())
print(f.readline())