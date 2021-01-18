#f=open("write1.txt","w")

#f.write("Hello")
#f.close()

#f=open("write1.txt","a")
#f.write("bye\n")
#f.close()

f=open("write1.txt","r+")

print(f.read())
a=f.write("nihahao means Hello\n")
print(a)
f.close()

