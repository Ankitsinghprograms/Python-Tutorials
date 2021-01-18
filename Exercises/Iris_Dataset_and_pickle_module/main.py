import requests

import pickle

import os

chose=input("Enter r to read in file and Enter w to write in file [r/w]:\n\n")

print("\n")


if chose=="w":
	
	file_size=os.path.getsize("data.pkl")
	
	write_=True
	
	if file_size>0:
		
		write_chose=input("Data is already save in file Do you want to Rewrite in file [y/n]\n\n")
		
		print("\n")

		
		if write_chose=="n":
			
			write_=True 
			

	if write_:
		
		print("Writing in File\n\n")
		
		website=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
		
		data=website.text
		
		rows=data.split("\n")
		
		save_data=[]
		
		for each in rows[:-2]:
			
			column=each.split(",")
			
			save_data.append(column)
			
		
		file_name="data.pkl"
		
		file=open(file_name,"wb")
		
		pickle.dump(save_data,file)
		
		print("Data saved in File succesfully\n\n")

else:
	
	try:
		file_name="data.pkl"
		
		file_size=os.path.getsize(file_name)
		
	except:
		
		print("File not Found!! \nPlease first Write something in it\n\n")
		
		exit()
	
	if file_size==0:
		
		print("Soory File is empty Please first Write something in it\n\n")
	
	else:
		
		print("Here is File data\n")
		
		file=open(file_name,"rb")
		
		data=pickle.load(file)
		
		print(data)
		