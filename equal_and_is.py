#== - Check value of object 
#is - check reference of object means memory mein dono ka location same hai ya nahi 



a=[1,12,3]
b=a
print(b is a,"Because both have same location in memory")

print(a==b,"Becuase both have same value")


a=[1,12,3]
b=list(a)
print(b is a,"Because both haven't same location in memory")

print(a==b,"Becuase both have same value")



