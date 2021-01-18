import pickle

#pickle.dumps()
#pickle.dump()
#pickle.load()
#pickle.loads()


#pickle.dumps()

l=[1,2,3,3,4,4,4,4,4,4,5,5,5,5,3,3,3,4,5,4,44,43,3,4,4]

data=pickle.dumps(l)

print(data)


#pickle.dump()
l=list(map(str,l))

file="pickle_data.pkl" 

file_obj=open(file,"wb")

pickle.dump(l,file_obj)

file_obj.close()

#pickle.load()
file="pickle_data.pkl" 

file_obj=open(file,"rb")


data=pickle.load(file_obj)

print(data)

file_obj.close()


#pickle.loads()

l=[1,2,3,3,4,4,4,4,4,4,5,5,5,5,3,3,3,4,5,4,44,43,3,4,4]

binary=pickle.dumps(l)

data=pickle.loads(binary)

print(data)